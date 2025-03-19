from django.shortcuts import render
from .models import Image

def main(r):
    photos = Image.objects.all()
    header_pic = photos.latest("date")
    photos = photos.exclude(id = header_pic.id)
    return render(r, "index.html", {'photos': photos, 'header_pic': header_pic})

def photography(r):
    return render(r, "photography.html")

def projects(r):
    return render(r, "projects.html")

def contact(r):
    return render(r, "contact.html")