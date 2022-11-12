# from fileinput import filename
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend
from django.core.files.storage import FileSystemStorage
import json
import os

FOLDER='static/files/'

def set_connection(username,password):
    backend = EmailBackend(host='smtp.gmail.com',port='587',username=username,password=password,use_tls=True)
    return backend

@api_view(["POST"])
def sendEmail(request):
    if request.method =="POST":
        try:
            rjson = json.loads(request.body)
            backend = set_connection(rjson['uname'],rjson['pass'])
            mail = EmailMessage(
                rjson['sub'],
                rjson['body'],
                rjson['uname'],
                [rjson['toEmail']],
                connection=backend
            )
            mail.send()
            print("Mail sent successfully")
            return Response({'message':"Mail sent successfully"})
        except Exception as e:
            print(e)
            return Response({'message':e})
    
@api_view(["POST"])
def sendEmailAttachment(request):
    global FOLDER
    if request.method =="POST":
        try:
            myfile = request.data['file']
            fs = FileSystemStorage(location=FOLDER)
            filename = fs.save(myfile.name,myfile)
            backend = set_connection(request.data['username'],request.data['password'])
            mail = EmailMessage(
                request.data['subject'],
                request.data['body'],
                request.data['username'],
                [request.data['to_email']],
                connection=backend
            )
            mail.attach_file(os.path.join("static","files/"+filename)) # check filename and put here
            mail.send()
            print("Mail sent successfully")
            os.remove(os.path.join("static","files/"+filename))
            return Response({'message':"Mail sent successfully"})
        except Exception as e:
            print(e)
            return Response({'message':e})