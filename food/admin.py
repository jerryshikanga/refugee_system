from django.contrib import admin
from .models import Food, DistributionUnit

# Register your models here.
admin.site.register(DistributionUnit)
admin.site.register(Food)