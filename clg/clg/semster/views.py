from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def semster1(request):
    res = render(request, 'semster/semster1.html')
    return res


def semster2(request):
    res = render(request, 'semster/semster2.html')
    return res


def semster3(request):
    res = render(request, 'semster/semster3.html')
    return res


def semster4(request):
    res = render(request, 'semster/semster4.html')
    return res


def semster5(request):
    res = render(request, 'semster/semster5.html')
    return res


def semster6(request):
    res = render(request, 'semster/semster6.html')
    return res


def semster7(request):
    res = render(request, 'semster/semster7.html')
    return res


def semster8(request):
    res = render(request, 'semster/semster8.html')
    return res

#subjectwise

def sem1sub(request):
    res = render(request, 'subject/sem1.html')
    return res

def sem2sub(request):
    res = render(request, 'subject/sem2.html')
    return res



def sem3sub(request):
    res = render(request, 'subject/sem3.html')
    return res

def sem4sub(request):
    res = render(request, 'subject/sem4.html')
    return res

def sem5sub(request):
    res = render(request, 'subject/sem5.html')
    return res

def sem6sub(request):
    res = render(request, 'subject/sem6.html')
    return res

def sem7sub(request):
    res = render(request, 'subject/sem7.html')
    return res

def sem8sub(request):
    res = render(request, 'subject/sem8.html')
    return res
