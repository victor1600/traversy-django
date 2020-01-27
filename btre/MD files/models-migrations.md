## Models

Under every app, there is a file named models.py, you can specify things like:
* class
* attributes
* Type of attributes
* Max length
* Required or not
* Foreing keys
* images:use model.ImageField(). There is a media folder, Everything we upload will go to that media folder. We set the location inside the media folder we want our images to go to.
* WE CANT SPECIFY THE DEFAULT FIELD WE WANT TO SHOW IN OUR ADMIN AREA USING THE STR METHOD

example:

```python
from django.db import models
from datetime import datetime

# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default = datetime.now, blank=True)

    def __str__(self):
        return self.name

```

## Migrations

### Create a migration

To create a migration, after written some code on the models, we type:

```python
python3 manage.py makemigrations
```
This will create a file inside each app, on the migrations folders that has defined a model. This folders
will have the structure like 000_initial.py and so on.

If we want to see the sql associated to the file, we type:

```python
python3 manage.py sqlmigrate listings 001
```

To migrate the files to the db:

```python
python3 manage.py migrate
```


