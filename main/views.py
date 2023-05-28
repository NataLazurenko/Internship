from datetime import datetime, timedelta

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Apply
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Applications
def index(request):
    if request.user.is_authenticated:
        if Applications.objects.all().filter(user=request.user).exists():
            application = Applications.objects.all().filter(user=request.user).last()
        else:
            application = None
    else:
        application = None
    return render(request, 'main/index.html', {'application': application})

@login_required
def apply(request):
    if request.method == "GET":
        form = Apply()
    else:
        form = Apply(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            age = application.age
            russian_citizenship = application.russian_citizenship
            application.user = request.user
            today = datetime.today()
            lastMonth = today - timedelta(days=90)
            if age >= 36 or age <= 17:
                application.recommended = False
            elif not russian_citizenship:
                application.recommended = False
            elif application.education == "other":
                application.recommended = False
            elif application.experience == "other":
                application.recommended = False

            elif Applications.objects.all().filter(user=request.user, archive=False, created__range=(lastMonth,today)).exists():
                application.recommended = False
                application.archive = True
            application.user = request.user
            application.save()
            return redirect("/")
        return redirect("/")
    return render(request, "main/apply/create.html", {"form": form})
