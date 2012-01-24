This is a fork of django-taggit-autocomplete (https://github.com/Jaza/django-taggit-autocomplete), adapted for working with http://code.drewwilson.com/entry/autosuggest-jquery-plugin

*** Installation ***

   1. You need to have django-taggit already installed
   2. Download django-taggit-autocomplete and use setup.py to install it on your system:
	python setup.py install
   3. Add "taggit_autocomplete" to installed apps in your project's settings.
   4. Add the following line to your project's urls.py file:
      (r'^taggit_autocomplete/', include('taggit_autocomplete.urls')),
   5. Install jQuery UI and a Theme
      ...if you are using Grappelli (highly recommended) then you already have jQuery UI in the Admin.
   6. Run ./manage.py collectstatic

*** Usage ***
** Using the model field **

You can use TaggableManager to enable autocompletion right in your models.py file. In most cases this is the easiest solution. Example:

from django.db import models
from taggit_autocomplete.managers import TaggableManager

class SomeModel(models.Model):
        tags = TaggableManager()
