from django.contrib import admin

# Register your models here.

from .models import Question

admin.site.register(Question)

# Register your models here.
from .models import GeeksModel
   
admin.site.register(GeeksModel)


# smtng
from .models import Musician
   
admin.site.register(Musician)

from .models import Album
   
admin.site.register(Album)