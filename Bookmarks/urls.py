"""
URL configuration for Bookmarks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main import views
from courses.views import CourseListView
urlpatterns = [
    path('', views.index, name="index"),
    path('apply/', views.apply, name='send_apply'),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('course/', include('courses.urls')),
    path('championship/', include('caseChampionship.urls')),
    path('course/all', CourseListView.as_view(), name='course_list'),
    path('students/', include('students.urls')),
    path('course/all', CourseListView.as_view(), name='course_list'),
    path('students/', include('students.urls')),
    path('employer/', include('employer.urls')),
    path('tutor/', include('tutor.urls')),
    path('room/', include('room.urls')),
    path('blog/', include('blog.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
