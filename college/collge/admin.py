from django.contrib import admin
from collge.models import College

class collegeAdmin(admin.ModelAdmin):
    list_display =['id','code','name','address']
    
admin.site.register(College,collegeAdmin)

