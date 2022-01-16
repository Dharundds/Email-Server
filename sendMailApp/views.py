from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    if request.method =="POST":
        send_mail(
            subject='test',
            message='This is a test',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['maladharunchennai@gmail.com']
        )
    return render(request,'index.html',{})