from django.shortcuts import render
from django.http import HttpResponse

def error_404_view(request,exception):
    return render(request,'ghar/404.html')
