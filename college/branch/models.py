from django.db import models

# Create your models here.


class Branch(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)


    def __str__(self):
        return "%s %s" % (self.name, self.description)