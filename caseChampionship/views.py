from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import Applications
from .models import Championship
from . import forms


@login_required
def send(request):
    if Applications.objects.all().filter(user=request.user).exists():
        application = Applications.objects.all().filter(user=request.user).last()
        if not Championship.objects.all().filter(application=application).exists():
            if request.method == "POST":
                form = forms.Championship(request.POST, request.FILES)
                if form.is_valid():
                    championship = form.save(commit=False)
                    championship.application = application
                    championship.save()
                return HttpResponse("успех")
            else:
                form = forms.Championship()
                return render(request, "caseChampionship/send.html", {'form': form})

        else:
            return HttpResponse("вывод ошибки(уже отправленно)")


    else:
        return HttpResponse("вывод ошибки")
