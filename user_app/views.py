from django.contrib.auth import login, logout
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View
from .forms import LoginFrom, RegisterForm
from .models import User


class LoginView(View):

    def get(self, request: HttpRequest):
        context = {'login_form': LoginFrom()}
        return render(request, 'login_page.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginFrom(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            remember = login_form.cleaned_data.get('remember_me')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if user.is_active:
                    is_pass_correct = user.check_password(user_password)
                    if is_pass_correct:
                        login(request, user)
                        if not remember:
                            request.session.set_expiry(0)
                        return redirect(reverse('home-page'))
                    else:
                        login_form.add_error('password', 'Invalid Password')
                else:
                    login_form.add_error('password', 'Please activate your account first')
            else:
                login_form.add_error('email', 'Email or password is incorrect')
        else:
            pass
        context = {'login_form': LoginFrom()}
        return render(request, 'login_page.html', context)


class LogoutView(View):
    def get(self, request: HttpRequest):
        logout(request)
        return redirect(self.request.META.get('HTTP_REFERER'))


class RegisterView(View):
    def get(self, request: HttpRequest):
        context = {'register_form': RegisterForm()}
        return render(request, 'register_page.html', context)

    def post(self, request: HttpRequest):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            email_exists = User.objects.filter(email__iexact=user_email).exists()
            if email_exists:
                register_form.add_error('email', 'Email already exists')
            else:
                new_user = User(
                    email=user_email,
                    email_active_code=get_random_string(72),
                    is_active=False,
                    username=user_email
                )
                new_user.set_password(register_form.cleaned_data.get('password'))
                new_user.save()
                return render(request, 'success.html')
        else:
            return render(request, 'error.html')
