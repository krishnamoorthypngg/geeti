from django.http import HttpResponse
from django.shortcuts import render
from web.models import Username,Password
def index(request):
    return (render(request,'file2.html'))
def user(request):
    return (render(request,'file2.html'))


