from django.contrib import admin
from .models import CarMake, CarModel, CarScanner

# Register your models here.
admin.site.register(CarMake)
admin.site.register(CarModel)
admin.site.register(CarScanner)
