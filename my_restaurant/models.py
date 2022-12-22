from django.db import models




class DaniRestaurant(models.Model):
    RestaurantName = models.CharField(max_length=200)
    RestaurantAddreess = models.CharField(max_length=200)
    FoodTypes = models.CharField(max_length=200)
    FoodPrice = models.DecimalField(max_digits=10, decimal_places=2)
    PhoneNumber = models.BigIntegerField()

    def __str__(self):
        return self.RestaurantName
    
class Customer(models.Model):
    food_industry = models.ForeignKey(DaniRestaurant, related_name="customer", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.BigIntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name="orders", on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    total_in_cents = models.IntegerField()

    def __str__(self):
        return self.description


