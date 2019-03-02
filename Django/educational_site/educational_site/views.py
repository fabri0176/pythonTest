from django.http import HttpResponse


def hello_worl(request):
    return HttpResponse('Hola Mundo desde Django')
