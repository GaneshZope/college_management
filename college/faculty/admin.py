from django.contrib import admin

from faculty.models import Faculty

class facultyAdmin(admin.ModelAdmin):
    list_display=['id','name','department','email_id','address']
    
admin.site.register(Faculty,facultyAdmin)
