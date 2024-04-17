from django.contrib import admin

from department.models import Department

class departmentAdmin(admin.ModelAdmin):
    list_display = ['id','college','code','name','building_no']

admin.site.register(Department,departmentAdmin)
