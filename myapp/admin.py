from django.contrib import admin

# Register your models here.

from .models import CustomUser

from django.contrib import admin
from .models import CustomUser

admin.site.register(CustomUser)