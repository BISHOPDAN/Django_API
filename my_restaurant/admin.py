from django.contrib import admin
from my_restaurant.models import Customer, Order, DaniRestaurant

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(DaniRestaurant)