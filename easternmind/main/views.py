from django.shortcuts import render
from .models import Image


def main(r):
    photos = Image.objects.all().reverse()

    for pic in photos:
        pic.date = pic.date.strftime("%I:%M %p")

    return render(r, "index.html", {"photos": photos})
