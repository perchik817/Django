from django.urls import path
from . import views
urlpatterns = [
    path('cars/', views.post_car,  name='post_car'),
    path('about_me/', views.about_me, name='about_me'),
]