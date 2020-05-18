from django.contrib import admin

# Register your models here.
from UserApp.models import *

admin.site.register(User)
admin.site.register(Post)
