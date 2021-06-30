

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def about(request):

    res = render(request, 'about/about.html')
    return res
