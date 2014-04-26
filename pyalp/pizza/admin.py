from django.contrib import admin

from pizza.models import Pizza, PizzaOrder

# Register your models here.
admin.site.register(Pizza)
admin.site.register(PizzaOrder)
