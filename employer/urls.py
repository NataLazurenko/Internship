from django.urls import path, include
from .import views

urlpatterns = [
    path('office/', views.office_page, name='office_page'),
]