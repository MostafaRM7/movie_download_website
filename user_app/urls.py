from django.urls import path
from .views import LoginView, LogoutView, RegisterView, DashboardView, FavoriteMovieView, RemoveFavoriteMovieView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login-page'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register-page'),
    path('dashboard/', DashboardView.as_view(), name='dashboard-page'),
    path('favorite-movie/', FavoriteMovieView.as_view(), name='favorite-movie'),
    path('remove-favorite-movie/', RemoveFavoriteMovieView.as_view(), name='remove-favorite-movie'),
]
