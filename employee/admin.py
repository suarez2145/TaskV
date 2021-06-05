from django.contrib import admin
from .models import Employee, Item, Worksite

admin.site.register(Employee)
admin.site.register(Worksite)
admin.site.register(Item)