from django.http import HttpResponse
from django.shortcuts import render


def hello_worl(request):
    return render(request, 'home.html')
