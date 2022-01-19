from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, "clinic/home.html", {})

def gallery(request):
  return render(request, "clinic/gallery.html", {})