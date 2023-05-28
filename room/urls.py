from django.urls import path
from . import views

urlpatterns = [
    path('create/',
             views.room_create,
             name='create_room'),
    path('<int:id>',
             views.get_room,
             name='get_room')
]