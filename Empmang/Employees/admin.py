from django.contrib import admin
from .models import *
admin.site.register(Department) # Department is class name present in models.py
admin.site.register(Employee)
