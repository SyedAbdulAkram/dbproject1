from django.shortcuts import render
from app1.models import Employee
# Create your views here.
def index(request):
    return render(request,'app1/index.html')
def empview(request):
    emp_list=Employee.objects.all()
    my_dict={'emp_list':emp_list}
    return render(request,'app1/emp.html',context=my_dict)