from django.shortcuts import render
from django.http import HttpResponse


def products(request):
    return HttpResponse("Hello world!")
    return HttpResponse(template.render())