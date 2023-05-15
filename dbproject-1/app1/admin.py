from django.contrib import admin
from app1.models import Employee
# Register your models here.
class Employeeadmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eaddr']
admin.site.register(Employee,Employeeadmin)