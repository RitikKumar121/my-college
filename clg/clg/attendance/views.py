

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def attendance(request):

    res = render(request, 'attendance/attendance.html')
    return res
