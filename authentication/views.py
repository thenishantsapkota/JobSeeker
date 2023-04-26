from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from .forms import LoginForm, RegisterForm

# Create your views here.


class RegisterView(View):
    form = RegisterForm

    def get(self, request):
        form = self.form()
        return render(request, "authentication/register.html", context={"form": form})

    @transaction.atomic
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "User registered successfully!")
            return redirect("login")
        return render(request, "authentication/register.html", context={"form": form})


class CompanyRegisterView(View):
    form = RegisterForm

    def get(self, request):
        form = self.form()
        return render(
            request, "authentication/register_employer.html", context={"form": form}
        )

    @transaction.atomic
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_user = False
            user.is_company = True
            user.save()
            messages.success(request, "User registered successfully!")
            return redirect("login")
        return render(
            request, "authentication/register_employer.html", context={"form": form}
        )


class UserLoginView(View):
    form = LoginForm

    def get(self, request):
        form = self.form()
        return render(request, "authentication/login.html", context={"form": form})

    def post(self, request: HttpRequest):
        form = self.form(request.POST)
        if form.is_valid():
            username = form.data.get("username")
            password = form.data.get("password")
            remember_me = form.data.get("remember_me")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                messages.success(request, "Logged in successfully!")
                return redirect("home")
            form.add_error("password", "Invalid username or password!")
        return render(request, "authentication/login.html", context={"form": form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Logged out successfully!")
        return redirect("home")
