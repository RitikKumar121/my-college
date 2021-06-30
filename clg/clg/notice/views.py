

from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
# Create your views here.


def notice(request):
    pics=Image.objects.all()
    res = render(request, 'notice/notice.html',{"pics":pics})
    return res
