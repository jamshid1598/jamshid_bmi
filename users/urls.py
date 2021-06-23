
from django.urls import path
from django.contrib.auth import views as auth_view

from .views import (
    NewUserCreationView, 
    login_view,
    logout_view,
)

# app_name = 'account'

urlpatterns = [
    path('signup/', NewUserCreationView.as_view(), name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # reset password viewes' urls
    path('password-change/', 
        auth_view.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), 
        name='password_change'),
    path('password_change_done/', 
        auth_view.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),
    path('reset_password/', 
        auth_view.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), 
        name='password_reset'),
    path('reset_password_sent/', 
        auth_view.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), 
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
        auth_view.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), 
        name='password_reset_confirm'),
    path('reset_password_complete/', 
        auth_view.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), 
        name='password_reset_complete'),
]