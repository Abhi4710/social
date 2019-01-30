## __Starting the Project Development:__


### Creating main Project structure:

Open command prompt and create a new folder User Management System and inside this folder create our main Project.

For creating the Main project folder.
__Syntax:__ 
```sh
django-admin startproject social
```
![Creating Project](../images/1.png)

### Migration and Running our server.

Open the newly created project using pycharm. You will find the screen as shown in the below image.

New project Structure.

### __Migrations:__ 
To map the models with the database we need to call the migrations method.
We are using the pycharm terminal for this. 
Refer to the below image.

__Syntax:__ 
```sh
python manage.py migrate.
```
This command will map the inbuilt models like auth, admin etc with the database.

### __Running the server:__ 
To run the server user the runserserver method.
__Syntax:__
```sh
python manage.py runserver
```
>Note: To close the running server use Ctrl + break inside the terminal.

### __Creating Super user & Accessing the admin Interface:__


#### __SuperUser:__ 
This will allow us to access the inbuilt admin panel of our webapp.
To create superuser use the createsuperuser method.
__Syntax:__
```sh
 python manage.py createsuperuser
 ```

Fill in the credentials for your superuser/admin account.








### __Login the admin interface:__

Open the admin interface by running the server and inside the browser type in the Url : 127.0.0.1:8080/admin

Login using your superuser username and password:





> Note: Create a directory named ‘templates’ inside the main project folder. We will be use this as our root directory to store/save templates.

Also make the following changes inside the settings.py file.
```sh
 TEMPLATES = [
'DIRS': [os.path.join(BASE_DIR, 'templates')],
 ]
 ```
 >Add this to the DIRS

refer to the below image.



### __Creating the base template:__

This base html file will be inherited by other templates. It will contain the features that are common among the templates.
IT save us from writing and editing the same code again and again, thus maintaining one of the golden rule of coding.

In this base template we are using bootstrap CDN. We will be adding a custom nav bar and as our project will develop based on the needs this will be modified.

__Code:__
```sh
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
   <title>base</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
          integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
</head>
<body style="background-color: ;">
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
 <a class="navbar-brand" href="#">Navbar</a>
 <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
   <span class="navbar-toggler-icon"></span>
 </button>
{% if user.is_authenticated %}
 <div class="collapse navbar-collapse" id="navbarSupportedContent">
   <ul class="navbar-nav mr-auto">
     <li class="nav-item active">
       <a class="nav-link" href="home">Home <span class="sr-only">(current)</span></a>
     </li>
     <li class="nav-item">
       <a class="nav-link" href="logout">Logout</a>
     </li>
     <li class="nav-item">
       <a class="nav-link " href="profile">Profile</a>
     </li>
     <li class="nav-item">
       <a class="nav-link" href="edit_profile">EditProfile</a>
     </li>
<li class="nav-item">
       <a class="nav-link" href="userdelete">DeleteProfile</a>
     </li>
   </ul>
 </div>
   {% else %}
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
   <ul class="navbar-nav mr-auto">
     <li class="nav-item active">
       <a class="nav-link" href="home">Home <span class="sr-only">(current)</span></a>
     </li>
     <li class="nav-item">
       <a class="nav-link" href="login">Login</a>
     </li>
     <li class="nav-item">
       <a class="nav-link" href="register">Register</a>
     </li>
   </ul>
 </div>
   {% endif %}
</nav>
{% block body %}
{% endblock %}
</body>
</html>
```

### __Integrating Allauth__
Django- Allauth allows us to add the social login feature to our web application. Users can login using their social id,s 
All-auth supports a lot number of social proves. Here we a going to use facebook as a social login provider.

__To use Allauth.__
__Steps:__

Install python package :
```sh
pip install django-allauth 
```

Configure Alluth in Project settings.py file.
```sh
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Already defined Django-related contexts here

                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    ...
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    ...
)

INSTALLED_APPS = (
    ...
    # The following apps are required:
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'Allauth.socialaccount',

SITE_ID = 2.  # depends on you site sequence
```
>Note: Also add the following code to specify which site id are you using for authentication.
Source: https://django-allauth.readthedocs.io/en/latest/installation.html

###__Facebook Authentication:__
Using django-Allauth we will use facebook to allows users to sign in to our website.
For this we will need to first configure the social account through our admin portal.

__Steps:__

1. Login into your django websites admin panel.
2. Goto social account administration. Click Add new social application.
3. Select Facebook as the social provider and Name will also be facebook.
4. Now log in facebook developer and click create a new App
5. Select Facebook Login as the product and the WWW as your platform.
6. In the next window Provide with your Site url.
> NOte: In our case it will be https://127.0.0.1/8080.
7. Save it and then skip the rest steps. 
8. Now we need to configure this facebook apps client id and secret key inside our social account.
9. We will find the client id and secret key inside the app/settings/basic
10. Just copy and paste in our admin social account.
11. Done Click save.

To load social account in a webpage use the following inside the template.
```sh
{% load socialaccount %}
<div align="center">
   <h1>OR</h1><br />
   <h2>Sign in using Your Facebook Account.</h2><br />
   <h1><a href="{% provider_login_url 'facebook' %}" >Facebook </a></h1>
</div>
```
>Note: Facebook authentication works on https not on http so you need to configure your development server to run on http using pyOpenSSL.

### __Install PyopenSSL__

using pip.
```sh
 pip install pyopenssl)
```
And run the server using 
```sh
python manage.py runsslserver
```



### __SSl Integration:__

We can use pyOPENSSL to run or test our projects on ssl server.
It allows us to run our project on https instead of http. All we need to do is to add the certificates and key in our browser.
These certificates and keys are generated when we install the pyOPENSSl.

__Steps:__
To install pyOPENSSL use PIP.
```sh
Syntax: PIP install pyopenSSl
```
This will install pyOpenSSl.

Add “sslserver” inside your main python project. Inside settings.py file.
```sh
INSTALLED_APPS= [
-----
-----
'sslserver',
]
```
Now open terminal and runserver using the following code:
__Syntax:__
```sh
 python manage.py runsslserver
``` 
Done.
>Note: the server is running over https instead of http.
