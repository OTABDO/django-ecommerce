from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [

    path('register/', views.register, name="register"),

    # Email verification URLs

    path('email-verification/<str:uidb64>/<str:token>', views.email_verification, name="email-verification"),
    path('email-verification-sent/', views.email_verification_sent, name="email-verification-sent"),
    path('email-verification-success/', views.email_verification_success, name="email-verification-success"),
    path('email-verification-failed/', views.email_verification_failed, name="email-verification-failed"),

]

