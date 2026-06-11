# Django Setup

> Works in Command Prompt only

## Steps

1. Create a virtual environment
   ```bash
   py -m venv firstenv
   .\firstenv\Scripts\activate
   ```

2. Install Django
   ```bash
   pip install django
   ```

3. Create a project
   ```bash
   django-admin startproject firstproject
   cd firstproject
   ```

4. Create an app
   ```bash
   py manage.py startapp firstapp
   ```

5. Register the app in the project files
   - Add the app name in `settings.py`
   - Update `urls.py` in the project folder if needed

6. Run the server
   ```bash
   py manage.py runserver
   ```

## Extra Notes

// create urls.py in firstapp
```python
from django.urls import path, include

path('', include('firstapp.urls'))
```

// create templates folder in firstapp
```python
'DIRS': [BASE_DIR / 'templates'],  # in settings.py
```

// code is written in views.py
```python
import redirect
```

// in urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage)
]
```

-in views 
  def homepage(request):
    return render(request,'home.html') 

// in templates create home.html

// urls ill call cheyyum, views ill link cheyyum

// templates --> all html loading codes

// <a href="{% url 'index' %}"></a>   linking url

// html tags
// a tag - linking (anchor tag)
// h tag - heading (1 to 3 size)
// p - paragraph
// img - image
// div - division
// btn - button tag
// br - break
// form - registration form

---models
  1.create model in model.py
  2.views ill updete

               def student(request):
            student=student.object.all()
            return render(request,'student.html')
            
  3.admin.py ill register

            admin.site.register(Student)


--admin
 py manage.py makemigrations
 py manage.py migrate
 py manage.py createsuperuser
 