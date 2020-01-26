Let's take a look at the about page:

```html
{% extends 'base.html'%}
{% load static %}
{% block content %}
 <!-- Breadcrumb -->
 <section id="bc" class="mt-3">
    <div class="container">
      <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
          <li class="breadcrumb-item">
            <a href="{% url 'index' %}">
              <i class="fas fa-home"></i> Home</a>
          </li>
          <li class="breadcrumb-item active"> About</li>
        </ol>
      </nav>
    </div>
  </section>

{% endblock %}

```

You'll se that is referencing to index page, where does that name come from?

> You define the name used for links inside urls.py of each app.

```python
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about')
]
```

### Highlight a selected link:

Example in _navbar.html:

```html
 {% load static %}
 <!-- Navbar -->
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary sticky-top">
    <div class="container">
      <a class="navbar-brand" href="{% url 'index' %}">
        <img src="{% static 'img/logo.png'%}" class="logo" alt="">
      </a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <ul class="navbar-nav">
          <li 
            {% if '/' == request.path  %}
              class="nav-item active mr-3"
            {% else %}
              class="nav-item mr-3"
            {% endif %}
          >
            <a class="nav-link" href="{% url 'index' %}">Home</a>
          </li>
          <li 
            {% if 'about' in request.path  %}
              class="nav-item active mr-3"
            {% else %}
              class="nav-item mr-3"
            {% endif %}
          >
            <a class="nav-link" href="{% url 'about' %}">About</a>
          </li>
          <li 
            {% if 'listings' in request.path  %}
              class="nav-item active mr-3"
            {% else %}
              class="nav-item mr-3"
            {% endif %}
          >
            <a class="nav-link" href="{% url 'listings' %}">Featured Listings</a>
          </li>
        </ul>

```