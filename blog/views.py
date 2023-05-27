from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
def hello_view(request):
    return HttpResponse('hello django :)')

def post_car(request):
    car = models.Cars.objects.all()
    return render(request, 'post_car.html', {'car':car})

def about_me(request):
    about = models.About.objects.all()
    return render(request, 'about_me.html', {'about': about})