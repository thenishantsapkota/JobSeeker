from django.urls import path

from .views import CompanyRegisterView, LogoutView, RegisterView, UserLoginView

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("company-register/", CompanyRegisterView.as_view(), name="company-register"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
