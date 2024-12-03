from django.shortcuts import render


def index(request):
    return render(request, "homepage/home.html")


def test(request):
    return render(request, "homepage/test.html")
