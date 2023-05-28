from django.urls import path, include
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('login/', views.user_Login, name='login'),
    path('apply/list/recommended/', views.dashboard_recommended_list, name="recommended_list"),
    path('apply/list/', views.dashboard_apply_list, name="apply_list"),
    path('apply/list/not-recommended/', views.dashboard_not_recommended_list, name="not_recommended_list"),
    path('tests/', views.dashboard_tests_choice, name="test_choice"),
    path('tests/give/<str:subject>/', views.dashboard_tests_list, name="tests_give"),
    path('export/', views.dashboard_export),
    path('career/list/', views.dashboard_career_list, name="career_list"),
    path('tests/accept/<int:id>/', views.accept_application),
    path('apply/view/<int:id>', views.view_application, name="view_application"),
    path('intern/', views.dashboard_intern, name="intern"),
    path('championship/download/<int:id>/', views.championship_download_file, name="championship_download"),
    path('championship/list/', views.championship_list, name="championship_list"),
    path('', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password-change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password-reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password-reset/complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('password-reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('register/', views.register, name='auth_register'),
    path('edit/', views.edit, name='edit'),
    path('', include('django.contrib.auth.urls')),
]
