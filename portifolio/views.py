from django.shortcuts import render


def home(request):
    return render(request, "portifolio/home.html")

def resume(request):
    return render(request, "portifolio/resume.html")

def contact(request):
    return render(request, "portifolio/contact.html")

