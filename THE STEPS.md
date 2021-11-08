## repodan cekme:
# Clone this repository
$ git clone https://github.com/your-user-name/your-project-name

# Install dependencies
    $ python -m venv env
    > env/Scripts/activate (for win OS)
    $ source env/bin/activate (for macOs/linux OS)
    $ pip install -r requirements.txt

# Run the app
$ python manage.py runserver

#### make a new project ###

```bash
# CREATING VIRTUAL ENVIRONMENT
# windows
py -m venv env
# windows other option
python -m venv env
# linux / Mac OS
vitualenv env

# ACTIVATING ENVIRONMENT
# windows
.\env\Scripts\activate
# linux / Mac OS
source env/bin/activate

# PACKAGE INSTALLATION
# if pip does not work try pip3 in linux/Mac OS
pip install django
# alternatively python -m pip install django
pip install python-decouple
django-admin --version
django-admin startproject forms .
```

add a gitignore file at same level as env folder

create a new file and name as .env at same level as env folder

copy your SECRET_KEY from settings.py into this .env file. Don't forget to remove quotation marks from SECRET_KEY

```
SECRET_KEY = django-insecure-)=b-%-w+0_^slb(exmy*mfiaj&wz6_fb4m&s=az-zs!#1^ui7j
```

go to settings.py, make amendments below

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
```

go to terminal

```bash
py manage.py migrate
py manage.py runserver
```

# the_step_of_new_project

1 python -m venv env
2 pip install django
3 .\env\Scripts\activate
4 pip install django
5 django-admin startproject main .
6 py manage.py startapp app   ' main/settings e git => 'INSTALLED_APPS = [ ekle]
7 pip install python-decouple
8 pip freeze > requirements.txt
9 py manage.py migrate
10 py manage.py createsuperuser
11 py manage.py runserver

# ################    models    ######################################

# app/models.py => 

  'from django.db import models

<!-- # Create your models here. -->
class Creater(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
class Language(models.Model):
    name = models.CharField(max_length=30)
    creator = models.OneToOneField(Creater, on_delete=models.CASCADE)

' py manage.py makemigrations ' => 
 ' 
 Migrations for 'dj_relations':
  dj_relations\migrations\0001_initial.py
    - Create model Creater
    - Create model Language
    '
# python hazırlıklarını yaptı:
' py manage.py migrate '
# dj_relations/admin.py ;
' from django.contrib import admin
from .models import Creator, Language
<!-- # Register your models here. -->
admin.site.register(Creator)
admin.site.register(Language)
# artık bunları admin panelde görebiliyorum.


# ####################### A simple view      ##############################

Here’s a view that returns a simple HTML document:

# import:
# from django.http import HttpResponse

def home_view(request):
    html = "<html><body>Hello World!</body></html>"
    return HttpResponse(html)


# rendering an html page:
# import:
# from django.shortcuts import render

def home_view(request):
    # There will be a context, we will use it on the html page.
    context = {
        'first_name': 'Rafe',
        'last_name': 'Stefano',
    }    
    return render(request, "app/home.html", context)
```

- Go to projenin(main)/urls.py and add:
```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("app.urls")), ( oluşturduğumuz app in urls ne git demek)
]
```
- Create urls.py under app, and add:
```py
from django.urls import path
from .views import home_view

urlpatterns = [
    path('', home_view, name="home"), (home_view app in altında functionun ismi)
]
```
- Go to settings.py and add under INSTALLED_APPS:
```py
'app.apps.FirstappConfig'  # or
'app'
```
# ####################### the end of A simple view      ##############################
# #######################   templates      ##############################
# app/views.py

from django.shortcuts import render

def home(request):
    # There will be a context, we will use it on the html page.
    context = {
        'first_name': 'Rafe',
        'last_name': 'Stefano',
    }    
    return render(request, "app/home.html", context)

# app/templates/app/home.html
The syntax of the Django template language involves four constructs.
- Variables
- Tags
- Filters
- Comments

### Variables

A variable outputs a value from the context, which is a dict-like object mapping keys to values.

Variables are surrounded by {{ and }} like this:

```py
My first name is {{ first_name }}. My last name is {{ last_name }}.
```

With a context of ```{'first_name': 'Rafe', 'last_name': 'Stefano'}```, this template renders to:

```py
My first name is Rafe. My last name is Stefano.
```

Dictionary lookup, attribute lookup and list-index lookups are implemented with a dot notation:

```py
{{ my_dict.key }}
{{ my_object.attribute }}
{{ my_list.0 }}
```


### Tags
[Tags reference](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#ref-templates-builtins-tags)

Tags provide arbitrary logic in the rendering process.

This definition is deliberately vague. For example, a tag can output content, serve as a control structure e.g. an “if” statement or a “for” loop, grab content from a database, or even enable access to other template tags.

Tags are surrounded by {% and %} like this:

```py
{% csrf_token %}
```
[csrf token reference](https://docs.djangoproject.com/en/3.2/ref/csrf/)

Most tags accept arguments:

```py
{% cycle 'odd' 'even' %}
```

Some tags require beginning and ending tags:

```html
{% if user.is_authenticated %}
    Hello, {{ user.username }}.
{% endif %}
```
### Tags: {% tag %}
- Some tags require beginning and ending tags:
```html
{% if %}
{% endif %}


{% if my_list %}
    print("List is not empty")
{% endif %}


{% for num in my_list %}
    <li>{{ num }}</li>
{% endfor %}
```

A reference of built-in tags is available as well as instructions for writing custom tags.


### Filters
[Filters reference](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#ref-templates-builtins-filters)

Filters transform the values of variables and tag arguments.

They look like this:

```py
{{ django|title }}
```

With a context of {'django': 'the web framework for perfectionists with deadlines'}, this template renders to:

```txt
The Web Framework For Perfectionists With Deadlines
```

Some filters take an argument:

```py
{{ my_date|date:"Y-m-d" }}
```

Note that you don't have to memorize this filters. Always look at the documentation, and create your hands-on notes to easy access your frequently used filters. For ```date``` here is the documentation:

[Drango filter: date](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#date)

A reference of built-in filters is available as well as instructions for writing custom filters.


### Comments

Comments look like this:

```
{# this won't be rendered #}
```

A {% comment %} tag provides multi-line comments.

### static

app/static/app/style.css =>
body{
    background-color: aquamarine;
}

app/templates/app/home.html =>
{% load static %}
 <head>
     <link rel="stylesheet" href="{% static 'app/style.css' %}">
 </head> 

 <img src="{% static 'app/django.jpg' %}" alt="resim">

# #########################   forms  ####################################
back end demek yarısı db demek:
database; veri tutma, işlenmesi, gönderilmesi vs işlemleri, ihtiyaç sahiplerine gönderilmesi 
database de tablolar var. öğrenci tablosu öğretmen tb vs gibi
modeller bu tablolara karşılık geliyor.  
django bizim yerimize database işlemlerini hallediyor. hangi aracı kullanıyor.arkaplanda bir database çalışıyor.bizim yazdıklarımızı orm hallaediyor. biz orm kodları yazıyoruz o hallediyor.
=> views : request geliyor ona göre görüntü döndürüyoruz. bir responsla karşı dönüyor
=> template :html,css


# ### forms:


kullanıcıdan bilgi almak için form kullanırız.
html form örneği;

<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname">
</form>
 django derki: benim form classlarımı kullana bilirsin.
 model class larfa çok benziyor. 

 
go to terminal, stop project, add app

```
py manage.py startapp student
```

go to settings.py and add 'student' app to installed apps and add below lines

```python
import os
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

create these folders at project level as /media/profile_pics

go to students/models.py

```python
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

```

go to terminal

```bash
pip install pillow
pip freeze > requirements.txt
py manage.py makemigrations
py manage.py migrate
```

create template folder as student/templates/student

base.html

```html
<!DOCTYPE html>
{% load static %}
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <!-- <link rel="stylesheet" href="../static/css/style.css" /> -->
    <link rel="stylesheet" href="{% static 'student/css/style.css' %}" />
  </head>
  <body>
    {% block container %}{% endblock container %}
  </body>
</html>
```

index.html

```html
{% extends "student/base.html" %} {% block container %}
<h1>Home Page</h1>

<h3>Student App</h3>

{% endblock container %}
```

student.html

```html
{% extends "student/base.html" %} {% block container %}
<form action="">
  <label for="">student name</label>
  <input type="text" />
  <input type="submit" value="OK" />
</form>
{% endblock container %}
```

go to student/views.py

```python
from django.shortcuts import render

def index(request):
    return render(request, 'student/index.html')

def student_page(request):
    return render(request,'student/student.html')

```

go to forms/urls.py

```python
from django.contrib import admin
from django.urls import path, include

from student.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('student/', include('student.urls')),
]
```

go to student/urls.py

```python
from django.urls import path

from .views import student_form

urlpatterns = [
    path('', student_form, name='student'),
]
```

run server and explain urls and form.html

go to students/forms.py

```python
from django import forms
from .models import Student

class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    number = forms.IntegerField(required=False)
```

go to student/views.py and amend student_page

```python
from .forms import StudentForm

def student_page(request):
    	form = StudentForm()
    	context = {
        	'form': form
    	}
    return render(request,'student/student.html', context)
```

explain sending form

go to student/templates/student/student.html and amend below lines

```html
% extends "student/base.html" %} {% block container %}

<h2>Student Form</h2>

{% comment %}
<form action="">
  <label for="">student name</label>
  <input type="text" />
  <input type="submit" value="OK" />
</form>
{% endcomment %}

<form action="" method="post" enctype="multipart/form-data">
  {% csrf_token %} {{ form.as_p }}
  <input type="submit" value="OK" />
</form>

{% endblock container %}
```

explain get, post, enctype and CSRF

go to student/forms.py and amend StudentForm and use forms.ModelForm class

```python
from .models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "number", "profile_pic"]
        labels = {"first_name": "Name"}
```

go to student/views.py and amend student_page

```python
def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student_data = {
                "first_name": form.cleaned_data.get('first_name'),
                "last_name": form.cleaned_data.get('last_name'),
                "number": form.cleaned_data.get('number')
                # "profile_pic": form.cleaned_data.get('profile_pic'),
            }
            # database save process
            # student = Student(first_name=student_name,
            #                   last_name=student_surname, number=student_number, mentor=student_mentor)
            student = Student(**student_data)
            if 'profile_pic' in request.FILES:
                student.profile_pic = request.FILES['profile_pic']
            student.save()
            return redirect('student')

    form = StudentForm()
    context = {
        'form': form
    }
    return render(request, 'student/student.html', context)
```

explain POST, and how to save student

go to terminal

```bash
py manage.py createsuperuser
```

navigate to admin panel and show that student model does not exist

go to student/admin.py

```python
from django.contrib import admin

from .models import Student
# Register your models here.
admin.site.register(Student)
```

navigate to admin panel and show student model there and display recorded students

go to student/views.py and amend student_page

```python
def student_form(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/student/')

    context = {
        'form': form
    }
    return render(request, 'student/student.html', context)
```

explain form.save and request FILES

## BOOTSTRAP

go to student/templates/student/base.html and add bootstrap

```html
<!DOCTYPE html>
{% load static %}
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <!-- <link rel="stylesheet" href="../static/css/style.css" /> -->
    <link rel="stylesheet" href="{% static 'student/css/style.css' %}" />
    <!-- CSS only -->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
      crossorigin="anonymous"
    />
  </head>

  <body>
    <div style="margin-top: 100px; margin-bottom: 100px" class="container">
      {% block container %}{% endblock container %}
    </div>
    <!-- JavaScript Bundle with Popper -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

## CRISPY FORMS

go to terminal

```bash
pip install django-crispy-forms
pip freeze > requirements.txt
```

go to settings.py

```python
INSTALLED_APPS = (
    ...
    'crispy_forms',
)

CRISPY_TEMPLATE_PACK = 'bootstrap4'
```

go to student/templates/student/student.html and crispy tags

```html
{% extends "student/base.html" %} {% block container %}

<h2>Student Form</h2>

{% comment %}
<form action="">
  <label for="">student name</label>
  <input type="text" />
  <input type="submit" value="OK" />
</form>
{% endcomment %}
<div style="width:300px;">
  {% load crispy_forms_tags %}
  <form action="" method="post" enctype="multipart/form-data">
    {% csrf_token %} {% comment %} {{ form.as_p }} {% endcomment %} {{ form |
    crispy}}
    <input type="submit" value="OK" />
  </form>
</div>
{% endblock container %}
```

## Messages

go to student/views.py and import messages end send success message

```
# from django.contrib import messages
def student_form(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successful")
            return redirect('/student/')
    context = {
        'form': form
    }
    return render(request, 'student/student.html', context)
```

go to student/templates/student/base.html and add messages codes

```html
<!DOCTYPE html>
{% load static %}
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <!-- <link rel="stylesheet" href="../static/css/style.css" /> -->
    <link rel="stylesheet" href="{% static 'student/css/style.css' %}" />
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>

<body>
    <div style="margin-top: 10px; margin-bottom: 10px" class="container">
        {% if messages %}
        {% for message in messages %}
        {% if message.tags == "error" %}
        <div class="alert alert-danger">{{ message }}</div>
        {% else %}
        <div class="alert alert-{{ message.tags }}">{{ message }}</div>
        {% endif %}
        {% endfor %}
        {% endif %}
        {% block container %}{% endblock container %}
    </div>
    <!-- JavaScript Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous">
    </script>
    </script>
    <script src="{% static 'student/js/timeout.js' %}"></script>
</body>

</html>
```





