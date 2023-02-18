from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.utils.decorators import method_decorator
from django.views import View

from movie_app.models import Serie, Film
from .forms import LoginForm, RegisterForm
from .models import User


class LoginView(View):

    @staticmethod
    def get(request: HttpRequest):
        if request.user.is_authenticated:
            return redirect(reverse('home-page'))
        context = {'login_form': LoginForm()}
        return render(request, 'login_page.html', context)

    @staticmethod
    def post(request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            remember = login_form.cleaned_data.get('remember_me')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                is_pass_correct = user.check_password(user_password)
                if is_pass_correct:
                    if user.is_active:
                        login(request, user)
                        if not remember:
                            request.session.set_expiry(0)
                        return redirect(reverse('home-page'))
                    else:
                        login_form.add_error('password', 'Email is not activated')
                else:
                    login_form.add_error('password', 'Invalid Password')
            else:
                login_form.add_error('password', 'Email or Password is incorrect')
        else:
            login_form.add_error('email', 'Email or Password is incorrect')
        context = {'login_form': login_form}
        return render(request, 'login_page.html', context)


class LogoutView(View):
    def get(self, request: HttpRequest):
        logout(request)
        return redirect(reverse('home-page'))


class RegisterView(View):
    @staticmethod
    def get(request: HttpRequest):
        context = {'register_form': RegisterForm()}
        return render(request, 'register_page.html', context)

    @staticmethod
    def post(request: HttpRequest):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            email_exists = User.objects.filter(email__iexact=user_email).exists()
            if email_exists:
                register_form.add_error('email', 'Email already exists')
            else:
                if register_form.cleaned_data.get('password') != register_form.cleaned_data.get('confirm_password'):
                    register_form.add_error('confirm_password', 'Passwords does not match')
                else:
                    new_user = User(
                        email=user_email,
                        email_active_code=get_random_string(72),
                        is_active=False,
                        username=user_email
                    )
                    new_user.set_password(register_form.cleaned_data.get('password'))
                    new_user.save()
                    login(request, new_user)
                    return redirect(reverse('dashboard-page'))
        return render(request, 'register_page.html', {'register_form': register_form})


@method_decorator(login_required(), name='dispatch')
class DashboardView(View):
    @staticmethod  # TODO: add user profile
    def get(request: HttpRequest):
        user = request.user
        saved_films = user.saved_films.all()
        saved_series = user.saved_series.all()
        return render(request, 'dashboard.html',
                      {'user': user, 'saved_films': saved_films, 'saved_series': saved_series})

    @staticmethod
    def post(request: HttpRequest):
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.email = request.POST.get('email')
        user.last_name = request.POST.get('last_name')
        user.save()
        return redirect(reverse('dashboard-page'))


@method_decorator(login_required(), name='dispatch')
class FavoriteMovieView(View):
    @staticmethod
    def get(request: HttpRequest):
        slug = request.GET.get('slug')
        user = request.user
        serie = Serie.objects.filter(slug=slug).first()
        if slug is not None and user is not None:
            if serie is not None:
                user.saved_series.add(serie)
                return JsonResponse({'success': True})

            film = Film.objects.filter(slug=slug).first()
            if film is not None:
                user.saved_films.add(film)
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False})
        else:
            return JsonResponse({'success': False})


@method_decorator(login_required(), name='dispatch')
class RemoveFavoriteMovieView(View):
    @staticmethod
    def get(request: HttpRequest):
        slug = request.GET.get('slug')
        user = request.user
        serie = Serie.objects.filter(slug=slug).first()
        if slug is not None and user is not None:
            if serie is not None:
                user.saved_series.remove(serie)
                return JsonResponse({'success': True})

            film = Film.objects.filter(slug=slug).first()
            if film is not None:
                user.saved_films.remove(film)
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False})
        else:
            return JsonResponse({'success': False})
