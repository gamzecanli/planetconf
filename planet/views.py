import datetime
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method=="POST":
        with open("blog.txt", 'a') as file:
            file.write("hello world")
    return render(request, "x.html")

def tarih_yaz(request):
    yazdimi="yazmadi"
    if request.method=="POST":
        with open("planetconf.txt","a") as file:
            tarih=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            file.write("\n"+tarih)
            yazdimi="yazdi "+tarih
    return render(request,"tarih.html",{"yazdimi":yazdimi})

