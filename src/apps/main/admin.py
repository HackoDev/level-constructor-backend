from django.contrib import admin
from solo.admin import SingletonModelAdmin

from apps.main import models

admin.site.register(models.Config, SingletonModelAdmin)
admin.site.register(models.Game)
admin.site.register(models.Location)
admin.site.register(models.Transition)
