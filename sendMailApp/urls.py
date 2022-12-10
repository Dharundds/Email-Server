from django.urls import path
from . import views


urlpatterns =[
    path('',views.home,name=''),
    path('sendplain',views.sendEmail,name='sendEmail'),
    path('sendAttachment',views.sendEmailAttachment,name='sendAttach'),
]