from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('account/register/',
         views.StudentRegistrationView.as_view(),
         name='register'),
    #path('enroll-course/',
    #    views.StudentEnrollCourseView.as_view(),
    #    name='student_enroll_course'),
     path('enroll-course/<int:course>/',
        views.student_enroll_course,
        name='student_enroll_course'),
    path('courses/',
         views.StudentCourseListView.as_view(),
         name='student_course_list'),
    path('course/<pk>/',
         cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
         name='student_course_detail'),
    path('course/<pk>/<module_id>/',
         cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
         name='student_course_detail_module'),

]