from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Participants)
admin.site.register(Club)
admin.site.register(participates)