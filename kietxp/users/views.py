from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserRegisterForm,UserProfileForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():


            user = form.save()
            user.is_active = False
            user.save()

            profile= profile_form.save(commit=False)



            profile.user =user
            profile.email = user.email

            profile.save()


            current_site = get_current_site(request)
            mail_subject = 'Activate your KXP account.'
            message = render_to_string('users/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            #return HttpResponse('Please confirm your email address to complete the registration')
            return render(request,'users/gmail_confirmation.html')




    else:
        form = UserRegisterForm()
        profile_form = UserProfileForm()


    return render(request,'users/register.html',{'form': form,'profile_form': profile_form})


def dashboard(request):
    return render(request,'users/dashboard.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return render(request,'users/gmail_confirmed.html')
    else:
        return HttpResponse('Activation link is invalid!')














