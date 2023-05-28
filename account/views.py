import datetime
import io
import os
from .decorators import has_group
import xlsxwriter
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, FileResponse
from django.contrib.auth import authenticate, login
from caseChampionship.models import Championship
from main.models import *
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages

def user_Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html',{'curator': True,'section': 'dashboard'})


@has_group("Curator")
def dashboard_recommended_list(request):
    applications = Applications.objects.all().filter(recommended=True, career=False)
    return render(request, 'account/dashboard/apply/list.html',
                  {'curator': True, 'section': 'apply', 'recommended': True, 'applications': applications})


@has_group("Curator")
def dashboard_not_recommended_list(request):
    applications = Applications.objects.all().filter(recommended=False, career=False)
    return render(request, 'account/dashboard/apply/list.html',
                  {'curator': True, 'section': 'apply', 'recommended': False, 'applications': applications})


@has_group("Curator")
def view_application(request, id):
    application = Applications.objects.get(pk=id)
    return render(request, 'account/dashboard/apply/view.html',
                  {'curator': True, 'section': 'apply', 'application': application})


@has_group("Curator")
def accept_application(request, id):
    application = Applications.objects.get(pk=id)
    application.career = True
    application.save()
    return JsonResponse({'message': 'success'}, safe=False)

@has_group("Curator")
def championship_download_file(request, id):
    application = Applications.objects.get(pk=id)
    if Championship.objects.all().filter(application=application).exists():
        championship = Championship.objects.get(application=application)
        file_path = os.path.join(settings.MEDIA_ROOT, championship.file.path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
        return HttpResponse('Выдаем ошибку')
    return JsonResponse({'message': 'success'}, safe=False)

@has_group("Curator")
def dashboard_apply_list(request):
    return render(request,"account/dashboard/apply/choice.html", {'curator': True, "section": "apply"})

@has_group("Curator")
def make_recommended(request,application):
    application = Applications.objects.get(id=application)
    application.recommended = True
    application.save
    return redirect("account:not_recommended_list")

@has_group("Curator")
def championship_list(request):
    if request.method == 'GET':
        championships = Championship.objects.all()
        return render(request, 'account/dashboard/championship/list.html',
                      {'section': 'championship', 'curator': True, 'championships': championships})
    elif request.method == "POST":
        application = request.POST.get("application")
        points = request.POST.get("points")
        application = Applications.objects.get(pk=application)
        if not Championship.objects.all().filter(application=application).exists():
            championship = Championship.objects.get(application=application)
            championship.percent = points
            championship.save()
        return redirect(f"/account/championship/list/")


@has_group("Curator")
def dashboard_tests_list(request, subject):
    if subject in ['russian','analysis','computer']:
        if request.method == 'GET':
            applications = Applications.objects.all().filter(test=True)
            return render(request, 'account/dashboard/test/list.html',
                          {"section": "tests", 'curator': True, 'applications': applications})
        if request.method == "POST":
            application = request.POST.get("application")
            points = request.POST.get("points")
            application = Applications.objects.get(pk=application)
            if not ApplicationTest.objects.all().filter(application=application, subject=subject).exists():
                test = ApplicationTest(application=application, value=points, subject=subject)

                test.save()
            return redirect(f"/account/tests/give/{subject}")
    else:
        return HttpResponse("ошибка 404")

@has_group("Curator")
def dashboard_career_list(request):
    if request.method == 'GET':
        applications = Applications.objects.all().filter(career=True)
        return render(request, 'account/dashboard/career/list.html',
                      {'curator': True,'section': 'career', 'applications': applications})
    if request.method == "POST":
        application = request.POST.get("application")
        points = int(request.POST.get("points"))
        print(points)
        application = Applications.objects.get(pk=application)
        if points >= 86:
            application.test = True
        application.career_percent = points
        application.save()
        return redirect(f"/account/career/list/")


@login_required
def dashboard_intern(request):
    applications = Applications.objects.all().filter(user=request.user).last()
    return render(request, "account/dashboard/intern/index.html", {'application': applications})


@has_group("Curator")
def dashboard_export(request):
    applications = Applications.objects.all()
    buffer = io.BytesIO()
    workbook = xlsxwriter.Workbook(buffer)
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'ФИО')
    worksheet.write('B1', 'Карьерная школа')
    worksheet.write('D1', 'Тестирование')

    worksheet.write('C2', 'Русский язык')
    worksheet.write('D2', 'Информационная граммотность')
    worksheet.write('E2', 'Анализ информации')
    worksheet.write('F2', 'Кейс чемпионат')
    m=2
    for i in applications:
        m+=1
        print(m)
        worksheet.write(f'A{str(m)}', i.user.first_name)
        if i.career_percent is not None:
            worksheet.write(f'B{str(m)}', f"{i.career_percent}%")
        else:
            worksheet.write(f'B{str(m)}', f"Не пройден")
        tests = ApplicationTest.objects.all().filter(application=i)
        try:
            worksheet.write(f'C{str(m)}', f'{tests.get(subject="russian").value}%')
        except Exception as e:
            print(e)
            worksheet.write(f'C{str(m)}', f'Не пройденно')

        try:
            worksheet.write(f'D{str(m)}', f'{tests.get(subject="computer").value}%')
        except Exception:
            worksheet.write(f'D{str(m)}', f'Не пройденно')

        try:
            worksheet.write(f'E{str(m)}', f'{tests.get(subject="analysis").value}%')
        except Exception:
            worksheet.write(f'E{str(m)}', f'Не пройденно')
        if  Championship.objects.all().filter(application=i).exists():
            champ = Championship.objects.get(application=i)
            if champ.percent is not None:
                worksheet.write(f'F{str(m)}', f'{champ.percent}%')
            else:
                worksheet.write(f'F{str(m)}', f'Не проверен')
        else:
            worksheet.write(f'F{str(m)}', f'Не пройден')

    worksheet.autofit()
    workbook.close()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f'report-{datetime.datetime.today().strftime("%Y-%m-%d")}.xlsx')


# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(user_form.cleaned_data['password'])
#             new_user.save()
#             return render(request, 'account/register_done.html',{'new_user': new_user})
#     else:
#         user_form = UserRegistrationForm()
#     return render(request, 'account/register.html', {'user_form': user_form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,'account/register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        return render(request,'account/register.html',{'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated'\
                                      'successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {'user_form': user_form,'profile_form': profile_form})


@has_group("Curator")
def dashboard_tests_choice(request):
    return render(request, "account/dashboard/test/choice.html", {'curator':True, "section": "tests"})
