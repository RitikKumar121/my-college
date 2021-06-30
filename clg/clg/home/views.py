from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def landing(request):
    res = render(request, 'home/home.html')
    return res
