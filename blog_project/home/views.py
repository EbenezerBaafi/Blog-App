from django.shortcuts import render, HttpResponse
# Create your views here.

def home(index):
    return HttpResponse("This is the home page of the blog application.")

def contact(index):
    return HttpResponse("This is the contact page of the blog application.")

def about(index):
    return HttpResponse("This is the about page of the blog application.")