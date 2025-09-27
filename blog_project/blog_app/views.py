from django.shortcuts import render, HttpResponse

# Create your views here.

def bloghome(index):
    return HttpResponse("This is the home page of the blog application.")

def blogpost(request, slug):
    return HttpResponse(f"This is the blog post:{slug}")