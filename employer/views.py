from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *


# Create your views here.


def office_page(request):
    if request.method == 'POST':
        form = RequestInternForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("OK, saved")
        else:
            return HttpResponse("форма не верная")
        # return HttpResponse(list(request.POST.items()))
    else:
        user_form = ApplicationForInternsForm()
        form = RequestInternForm
        return render(request, 'office/office.html', {'form': form, 'ages_list': OPTIONS_AGES, 'cities_list': OPTIONS_CITIES,
                                                      'universities_list': OPTIONS_UNIVERSITIES, 'directions_list': OPTIONS_DIRECTIONS,
                                                      'work_expirience_list': OPTIONS_EXPERIENCE_WORK, 'internship_direction_list': OPTIONS_INTERNSHIP_DIRECTIONS, 'user_form': user_form})
