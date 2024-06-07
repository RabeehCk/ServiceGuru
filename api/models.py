from django.db import models

from django.contrib.auth.models import User



class Customer(models.Model):

    name = models.CharField(max_length=200)

    email = models.CharField(max_length=200)

    phone = models.CharField(max_length=200)

    vehicle_number = models.CharField(max_length=200)

    running_km = models.PositiveIntegerField()

    technician = models.ForeignKey(User,on_delete=models.CASCADE)

    options = (

        ("pending","pending"),

        ("in-progress","in-progress"),

        ("completed","completed")
    )

    status = models.CharField(max_length=200,choices=options,default="pending")

    created_date = models.DateTimeField(auto_now_add=True)

    update_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:

        return self.name


class Work(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    amount = models.PositiveIntegerField()

    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)

    update_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:

        return self.title