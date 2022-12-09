from django.contrib import admin
from tasks.models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    admin.site.register(Task)
