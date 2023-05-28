from django.urls import path, include
from .import views

urlpatterns = [
    path('office-tutor/', views.office_page, name='office_page'),
    path('office-tutor/intern-sort/<int:id>', views.intern_sort, name='intern_sort'),
    path('office-tutor/set-mentor/', views.set_mentor_to_student, name='set_mentor'),
]