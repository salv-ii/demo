from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import games
def demo(request):
    obj=place.objects.all()
    sal=games.objects.all()
    return render(request,"index.html",{'result':obj,'sal':sal})

def about(request):

    return render(request,"about.html")