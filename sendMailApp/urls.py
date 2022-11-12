from django.urls import path
from . import views


urlpatterns =[
    path('sendplain',views.sendEmail,name='sendEmail'),
    path('sendAttachment',views.sendEmailAttachment,name='sendAttach'),
]