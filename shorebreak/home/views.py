from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home/index.html")
def contact(request):
    return render(request, "home/contact.html")
def carte(request):
    return render(request, "home/carte.html")
