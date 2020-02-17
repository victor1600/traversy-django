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

Notice the syntax ```views.methodName```

## Pass data to template

* We do that with a dictionary

```python
def index(request):
    return render(request, 'listings/listings.html', {
        'name': 'Brad'
    })
```


## Receive data in template

* Example:
```html
  <h1 class="display-4"> Browser our Properties {{ name }}</h1>
```


## Fetch data from DB and send it to template

* Put everything in 'context' dictionary
* send context argument to render method.

```python
def index(request):
    listings = Listing.objects.all()

    context = {
        'listings': listings
    }

    print(listings)

    return render(request, 'listings/listings.html',context)
```

## Show data retrieved from db in template

* Loop through the objects:

### Using humanize

* Go to main settings.py and add the following at the onf INSTALLED_APPS
array:

```python
'django.contrib.humanize'
```
* Go to the top of listings html and add the following after
 ```{% extends 'base.html' %}```:

````python
{% load humanize %}
````


**notice**:

* Use of humanize intcomma to display the comma in prices, and humanize
time since, to get time in human mode.
* Use of .url attribute of the image attribute of our listing.
* when using listing.realtor, the __str__method will get invoked, which
returns the name of the realtor.

```html

  <!-- Listings -->
  <section id="listings" class="py-4">
    <div class="container">
      <div class="row">
          {% if listings %}
              {% for listing in listings %}
                   <!-- Listing 1 -->
                <div class="col-md-6 col-lg-4 mb-4">
                  <div class="card listing-preview">
                    <img class="card-img-top" src="{{ listing.photo_main.url }}" alt="">
                    <div class="card-img-overlay">
                      <h2>
                        <span class="badge badge-secondary text-white">${{listing.price | intcomma }}</span>
                      </h2>
                    </div>
                    <div class="card-body">
                      <div class="listing-heading text-center">
                        <h4 class="text-primary">{{ listing.title }}</h4>
                        <p>
                          <i class="fas fa-map-marker text-secondary"></i> {{ listing.city }}
                            {{ listing.state }}, {{ listing.zipcode }}
                        </p>
                      </div>
                      <hr>
                      <div class="row py-2 text-secondary">
                        <div class="col-6">
                          <i class="fas fa-th-large"></i> {{ listing.sqft }}</div>
                        <div class="col-6">
                          <i class="fas fa-car"></i> {{ listing.garage }}</div>
                      </div>
                      <div class="row py-2 text-secondary">
                        <div class="col-6">
                          <i class="fas fa-bed"></i> {{ listing.bedrooms }}</div>
                        <div class="col-6">
                          <i class="fas fa-bath"></i> Bathrooms: 2</div>
                      </div>
                      <hr>
                      <div class="row py-2 text-secondary">
                        <div class="col-12">
                          <i class="fas fa-user"></i> {{ list.realtor }}</div>
                      </div>
                      <div class="row text-secondary pb-2">
                        <div class="col-6">
                          <i class="fas fa-clock"></i> {{ listing.list_data | timesince }}</div>
                      </div>
                      <hr>
                      <a href="{% url 'listing' listing.id %}" class="btn btn-primary btn-block">More Info</a>
                    </div>
                  </div>
                </div>
              {% endfor %}

          {% else %}
              <div class="col-md-12">
                <p>No listings Available.</p>
              </div>

          {% endif %}

      </div>
```

### Sending a parameter from one template to another

* Notice in the code above in the ```<a>``` we see the syntax to send
 an argument to other view.
* The listing method which we invoke, has to have as one of it's
argument, the expected value that will recieve from the other template:

```python
def listing(request, listing_id):
    return render(request, 'listings/listing.html')

```