from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello, Jovanni. You\'re at the Polls index! Hooray!")
