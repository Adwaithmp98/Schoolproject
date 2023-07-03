from django.contrib.auth import logout
from django.urls import path

from taskapp.views import register, login, demo, get_courses, index, save_form, Home

urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('index', index, name='index'),
    path('get_courses/<int:department_id>/', get_courses, name='get_courses'),
    path('', demo, name='demo'),
    path('Home', Home, name='Home'),
    path('save-form/', save_form, name='save_form'),


]
