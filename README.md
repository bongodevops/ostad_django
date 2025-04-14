# ostad_django
=> At first run:
    pipenv shell
=> Then:
    git chechout -b template
=> Then:
    myapp/templates/base.html
    myapp/templates/home.html
    myapp/templates/order.html
    myapp/templates/contact.html
    myapp/views.py
    myapp/urls.py  
=> Then:
    python manage.py startapp orderapp
    register orderapp in settings.py
    orderapp/urls.py
    orderapp/views.py
    templates/order.html
=> Then:
    python manage.py runserver
=> Then:
    HTML customization
=> Then:
    git add .
    git commit -m "template"
    git push origin template
