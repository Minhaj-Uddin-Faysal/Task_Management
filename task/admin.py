from django.contrib import admin

# Register your models here.
from .models import TaskModel,TaskCategory

admin.site.register(TaskModel)
admin.site.register(TaskCategory)
