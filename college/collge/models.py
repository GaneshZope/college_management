from django.db import models

class College(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    
    
