from django.http import HttpResponse


def index(request):
  return HttpResponse('Bienvenido a FullStack Python Index')