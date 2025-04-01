from django.shortcuts import render
from .models import Image


def main(r):
    photos = Image.objects.all()
    header_pic = photos.latest("date")
    photos = photos.exclude(id=header_pic.id)

    for pic in photos:
        pic.date = pic.date.strftime("%I:%M %p")

    return render(r, "index.html", {"photos": photos, "header_pic": header_pic})
