from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from room.forms import SetRoomForm
from room.models import Room
from tutor.models import SetMentorToStudent


@login_required
def room_create(request): # создание комнаты, здесь должен комнату создавать tutor (куратор)
    if request.method == 'POST':
        form = SetRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("OK, saved")
        else:
            return HttpResponse("форма не верная")
    else:
        form = SetRoomForm
        return render(request, 'set_room.html', {'form': form})


@login_required
def get_room(request, id): # получить комнату с заданием и ссылками
    id = id - 1
    form = Room.objects.all()
    user_id = request.user.id
    to_template = []
    for i in range(len(form)):
        if str(form[id].id_student) == str(user_id):
            to_template.append(form[id].id_mentor)
            to_template.append(form[id].id_student)
            to_template.append(form[id].text_task)
            to_template.append(form[id].task_links)
    return render(request, 'room.html', {'my_list': to_template})

# Create your views here.
