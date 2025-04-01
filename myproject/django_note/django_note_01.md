
# myproject create and runserver

1. folder create
2. cd folder
3. pipenv shell
4. pipenv install django
5. django-admin startproject project_Name .
6. python manage.py runserver
7. python manage.py migrate 
8. python manage.py runserver
9. python manage.py
10. python manage.py createsuperuser
    - username: hafiz
    - email: admin@hafiz.com
    - password:2200
11 . python manage.py runserver

# app_create and setting

12. python manage.py startapp myapp
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  # Your custom app
]
```

### myapp/views.py

```
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello, world!")

```
### myapp/urls.py

```
from django.urls import path
from . import views

urlpatterns = [
   path('hello/', views.say_hello, name='say_hello'), 
]
```

### myproject/urls.py

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('myapp.urls')), 
]
```

### create a new repository on the command line

echo "# ostad_django" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:bongodevops/ostad_django.git
git push -u origin main