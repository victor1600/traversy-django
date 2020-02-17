# Creating the base Template for the project



### Summary:
 * We have to use the ```{% load static %} ``` to access css and js.
 * In body tags we leave a section between ```{% block content %} {% endblock %} ``` tags. **Thats 
 where all the custom extended HTML will go.
 * We call partials with ```{% include 'partials/_navbar.html' %}``` syntax. 
 * Navbar annd Topbar go above  ```{% block content %}```.
 * Footer goes below it.


### Where should all css and JS must be placed?

* CSS in the ```head```
* Js in the bottom of the ```body``` tag

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="{% static 'css/all.css' %}">
    <!-- Bootstrap -->
    <link rel="stylesheet" href="{% static  'css/bootstrap.css' %}">
    <!-- Custom -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    <!-- Lightbox -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    <title> Bt Real Estate</title>
</head>
<body>
    <!--Top Bar-->
    {% include 'partials/_topbar.html' %}
    <!-- NavBar -->
    {% include 'partials/_navbar.html' %}

    {% block content %}
    {% endblock %}
    <!--   Footer -->
    {% include 'partials/_footer.html' %}
    <script src="{% static 'js/jquery-3.3.1.min.js' %}"></script>
    <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
    <script src="{% static 'js/lightbox.min.js' %}"></script>
    <script src="{% static 'js/main.js' %}"></script>
</body>
</html>
```


 ## How to create partial views:
 
 * Create a folder inside templates called partials
 * Create _navbar.html,_topbar.html, etc.
 
 **Example of content that should go there:**
 
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

        <ul class="navbar-nav ml-auto">
          <li class="nav-item mr-3">
            <a class="nav-link" href="register.html">
              <i class="fas fa-user-plus"></i> Register</a>
          </li>
          <li class="nav-item mr-3">
            <a class="nav-link" href="login.html">
              <i class="fas fa-sign-in-alt"></i>

              Login</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

```

