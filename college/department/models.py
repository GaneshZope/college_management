from django.db import models
from collge.models import College


class Department(models.Model):
    college = models.ForeignKey(College,on_delete=models.CASCADE)
    code = models.IntegerField()
    name = models.CharField(max_length=100)
    building_no = models.IntegerField()
    
    def __str__(self):
        return self.name
    