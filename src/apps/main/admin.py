from django.contrib import admin

from apps.main import models

admin.site.register(models.Game)
admin.site.register(models.Location)
admin.site.register(models.Transition)
