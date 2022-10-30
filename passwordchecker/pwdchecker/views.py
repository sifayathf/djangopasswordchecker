from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse ("Assalamu Aliakkum.")


def greeting(request):

    if(request.GET.get('length1',12)==''):
        return render (request, 'pwdchecker/greeting.html', {
            'nouns': 'Brothers and Sisters'
        })

    n= int(request.GET.get('length1',12))
    return render (request, 'pwdchecker/greeting.html', {
        'nouns': 'Brothers and Sisters'
        })

def greeting1(request):
    return render (request, 'pwdchecker/greeting1.html')