from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Contact
from django.contrib import messages
import json
import requests



def myghar(request):
    return render(request,'ghar/index.html')

def contact(request):
  if request.method=="POST":
    name=request.POST.get('name','')
    email=request.POST.get('email','')
    message=request.POST.get('message','')
    contact = Contact(name=name,email=email,message=message)

    clientkey = request.POST['g-recaptcha-response']
    secretkey = '6LdM9awZAAAAAG2CeOg9_M1RNS9KHmg7zEimnOpB'
    captchaData = {
          'secret': secretkey,
          'response': clientkey
              }
    r= requests.post('https://www.google.com/recaptcha/api/siteverify', data=captchaData)
    response = json.loads(r.text)

    if response['success'] == True:
        contact.save()
        messages.success(request, f' Hi {name}! We received your message and will respond shortly!')
        return HttpResponseRedirect("/")
    else:
         messages.warning(request, f' Ooops.... we do not allow robots!')
         return HttpResponseRedirect("/")

