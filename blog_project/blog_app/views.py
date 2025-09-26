from django.shortcuts import render, HttpResponse

# Create your views here.

def home(index):
    return HttpResponse("This is the home page of the blog application.")

def blog(index):
    return HttpResponse("This is the blog page of the blog application.")