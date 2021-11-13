from django.db import models

# Create your models here.
class Customer(models.Model):
    firstName = models.TextField(max_length=50)
    lastName = models.TextField(max_length=50)
    emailId = models.EmailField(max_length=100)
    mobileNo = models.IntegerField()
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f"{self.firstName} {self.lastName}"