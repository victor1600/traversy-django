# Static Folder

Create a static folder inside your main's app dir. Name it static and copy
all the assets you want to use. Create subfolders inside it (CSS,JS, images).

```python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'btre/static')
]
```

We created a static root and static file dirs.
Static root will create will create a static folder in root.

Type

```shell script
python3 manage.py collectstatic
```

That'll create a folder, that will be used in deployment.

## Referencing statif files inside templates

* Put in the beginning :```{% load static%}```
* Whenever you use a an image, js,css, use the following structure( subfolder-Inside-staticFolder/asset):
```html
 <img src="{% static 'img/about.jpg' %}" alt="">
```

