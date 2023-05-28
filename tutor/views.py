from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from account.models import Profile
from employer.models import RequestInternModel
from students.forms import StudentCreateForm
from students.models import Student
from tutor.forms import SetMentorToStudentForm


@login_required
def office_page(request): # Список заявок от работодателей на стажеров
    posts = RequestInternModel.objects.all()
    user_id = request.user.id
    posts_employer = []
    for i in range(len(posts)):
        if posts[i].id_tutor == str(user_id):
            posts_employer.append(str(posts[i].id_tutor) + ":" + str(posts[i].age) + ":" + str(posts[i].city)
                                  + ":" + str(posts[i].university) + ":" + str(posts[i].direction)
                                  + ":" + str(posts[i].work_experience)
                                  + ":" + str(posts[i].internship_direction))
    return HttpResponse(posts_employer)


@login_required
def intern_sort(request, id): # список стажеров подходящих по критериям, по id заявке работодателя
    id = id - 1
    posts = RequestInternModel.objects.all()
    filter_students = Student.objects.all().filter(age=posts[id].age, city=posts[id].city, university=posts[id].university,
                                 direction=posts[id].direction, work_experience=posts[id].work_experience,
                                 internship_direction=posts[id].internship_direction)

    posts_intern = []
    for i in range(len(filter_students)):
        posts_intern.append(str(filter_students[i].id_user) + ":" + str(filter_students[i].age) + ":" + str(filter_students[i].city)
                              + ":" + str(filter_students[i].university) + ":" + str(filter_students[i].direction)
                              + ":" + str(filter_students[i].work_experience)
                              + ":" + str(filter_students[i].internship_direction))
    return HttpResponse(posts_intern)


@login_required
def set_mentor_to_student(request): # назначить стажеру наставника
    if request.method == 'POST':
        form = SetMentorToStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("OK, saved")
        else:
            return HttpResponse("форма не верная")
    else:
        form = SetMentorToStudentForm
        return render(request, 'set_mentor.html', {'form': form})



# Create your views here.
