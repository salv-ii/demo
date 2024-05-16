from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    return render(request,"demo.html")


def contact(request):
    return HttpResponse("you can contact on 1234567890")
def details(request):
    return render(request,"details.html")
def thanku(request):
    return render(request,"thanku.html")

def addition(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    add=x+y
    sub=x-y
    pro=x*y
    div=x/y
    return render(request,"result.html",{'addition':add,'substraction':sub,'multiplication':pro,'division':div})