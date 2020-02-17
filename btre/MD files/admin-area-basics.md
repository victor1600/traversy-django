# Admin area Basics

If you want to see available options for python manage.py:

```shell script

python3  manage.py help
````

* Create a superuser.

### Creating listings through admin area

* Go to listings->admin.py

* import models(you can check name at models.py):
```from .models import Listing```

* Register a model(Inside admin.py from listings):

```python
admin.site.register(Listing)
```

You'll see listings option in admin area.

*Do the same for realtors.