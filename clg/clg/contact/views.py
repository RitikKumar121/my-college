from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def contact(request):
    res = render(request, 'contact/contact.html')
    return res
