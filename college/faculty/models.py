from django.db import models
from department.models import Department
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    email_id=models.EmailField()
    address=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
