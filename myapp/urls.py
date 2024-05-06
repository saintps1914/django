from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='../templates/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('index/', views.index, name='index'),
    path('', views.login_redirect, name='login_redirect'),  # Добавленный маршрут
    path('prompts/', views.prompts, name='prompts'),
    path('new_data/', views.new_data, name='new_data'),
]