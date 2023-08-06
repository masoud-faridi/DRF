from django.urls import path, include
from app_api_functions.views import welcome

urlpatterns = [
    path('welcome/', welcome, name='movie_list'),


]
