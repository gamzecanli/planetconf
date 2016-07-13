from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method=="POST":
        with open("blog.txt", 'a') as file:
            file.write("hello world")

    return render(request, "x.html")
