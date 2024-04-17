from django.db import models


# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    branch= models.CharField(max_length=10)
    birthdate = models.DateField()
    email = models.EmailField(max_length=254)
    year = models.IntegerField()
    contact = models.IntegerField()

    def __str__(self):
        return self.first_name


