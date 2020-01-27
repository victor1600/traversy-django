# Views

We have to define a method, that a route inside urls.py expects to find.

* All methods will have a request parameter.
* Most of the time, they'll return a rendered template

Without sending parameters to template:

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"pages/index.html")

def about(request):
    return render(request,"pages/about.html")

```

Let's take a look to urls.py:

```python
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about')
]
```

Notice the sytax ```views.methodName```