from django.contrib import admin
from .models import Part, Customer, Operation

# Register your models here.

admin.site.register(Customer)
admin.site.register(Part)
admin.site.register(Operation)