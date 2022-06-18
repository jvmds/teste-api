from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request):
    a = ""
    if request.method == 'POST':
        a = request.body
    print(a)
    return HttpResponse(a)
