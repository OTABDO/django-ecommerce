from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'
urlpatterns = [

    path('register/', views.register, name="register"),

    # Email verification URLs

    path('email-verification/<str:uidb64>/<str:token>', views.email_verification, name="email-verification"),
    path('email-verification-sent/', views.email_verification_sent, name="email-verification-sent"),
    path('email-verification-success/', views.email_verification_success, name="email-verification-success"),
    path('email-verification-failed/', views.email_verification_failed, name="email-verification-failed"),
    # Login Logout

    path('my-login/', views.my_login, name="my-login"),
    path('user-logout', views.user_logout, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),

    # Dashboard
    path('dashboard/', views.dashboard, name="dashboard"),
    path('profile-management/', views.profile_management, name="profile-management"),
    path('delete/', views.delete_account, name="delete-account"),


    # Password management urls views

    # 1) submit our email form
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name="account/password/password-reset.html",
                                                                 success_url=reverse_lazy('account:password_reset_done'),
                                                                 email_template_name="account/password/email-password.html"
                                                                 ),

         name='reset_password'),

    # 2) success message sent stating that the message sent
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="account/password/password-reset-sent.html"),
         name='password_reset_done'),

    # 3) Password reset link
    path('reset/<str:uidb64>/<str:token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="account/password/password-reset-form.html",
                                                     success_url=reverse_lazy('account:password_reset_complete')),
         name='password_reset_confirm'),

    # 4) Password reset success
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="account/password/password-reset-complete.html"),
         name='password_reset_complete'),


    # Manage shipping url
    path('manage-shipping/', views.manage_shipping, name='manage-shipping'),
    path('track-orders/', views.track_orders, name='track-orders'),
]

