from django.urls import path
from django.contrib.auth import views as auth_views

from.usuario_views import (login_user,  register, logout_user, activate, email_confirmation_sent, 
        UserEditView,password_change,password_changed, edit_profile,
        ShowProfilePageView, ProfileListView, follow_unfollow_profile)

urlpatterns = [
    
    path ('login/', login_user ),
    path('register/', register),
    path('logout_user/', logout_user),
    path('email_activation/', activate),
    path('email_confirmation_sent/', email_confirmation_sent),
    path('activate/<uidb64>/<token>/', activate, name='activate'),#path de la activacion del email

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset_password_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_done.html"), name="password_reset_complete"),

    path('password/',password_change.as_view(template_name="change_password.html")),
    path('password_changed/', password_changed),


    path('edit_user/', UserEditView.as_view(), name='edit_user'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile/', edit_profile, name='edit_profile'),

    path('suggested_users/', ProfileListView.as_view(), name='profile_list_view'),
    path('switch_follow/', follow_unfollow_profile, name='follow_unfollow_profile'),
]
