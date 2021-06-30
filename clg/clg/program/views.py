from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def program(request):

    res = render(request, 'program/program.html')
    return res
