# Email-Server

# How this app differ from normal email sending application

-> This app doesn't requires you to turn on less secure apps in your gmail acc\
-> Which means it is secure because your gmail actual password is not exposed


# Todo just after cloning
1) Ensure you have enabled google two-factor auth by navigating into https://myaccount.google.com/
2) then to security tab in the menu then scroll down to App passwords click and create one for your app
3) copy that password and keep it secure and this password is what we are going to use
4) reference how to create your app password -- https://support.teamgate.com/hc/en-us/articles/115002064229-How-to-create-a-password-to-connect-email-while-using-2-step-verification-in-Gmail-  
5) create a .env file inside sendEMail folder
    consisting of two variable
    1) EMAIL_HOST_USER=youremail@gmail.com
    2) EMAIL_HOST_PASSWORD=yourAppPassword

# Turn on sever
* cd to Email-server
* then open terminal or command prompt here
* now type `pipenv shell`\ if you don't have pipenv installed then pip install pipenv the type that command
* right after opening pipenv shell type `pipenv install`
* once done type ` python manage.py runserver ` to turn on the server
* after server is turned on navigate to http://127.0.0.1:8000

# How to use
* once you navigated to the site click on the send button email will be sent


