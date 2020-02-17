## Customizing admin area

### Create template

* Create a folder with name admin inside templates
and create base_site.html

### Override CSS

```html
{% block extrastyle %}
    <link rel="stylesheet" href="{% static 'css/admin.css' %}">
{% endblock %}
```

## Edit 'listar' in listings admin area

### Show custom fields in listar:

* Go to admin inside listings.app
* Create a class that inherits from model.ListingAdmin
* Create a list of fields you want to display
* Register the class.

### Clicking on item name and being redirected to 'details' page

* Add to the ListingAdminClass:

```python
 list_display_links = ('id','title')
```

### Filter box

```python
    list_filter = ('realtor', )
```

> If its only one value, we leave the comma at the end

### Set editable a boolean field(check and uncheck)

```python
list_editable = ('is_published')
```

### Searching by certain fields

```python
 search_fields = ('title','description', 'address', 'city', 'state', 'zipcode','price' )
```


### Pagination

```python
list_per_page = 25
```