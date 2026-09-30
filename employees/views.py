from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



EMPLOYEES = [
    {"id": 501, "name": "Rohan", "department": "IT", "designation": " Developer"},
    {"id": 502, "name": "Abhinav", "department": "HR", "designation": "HR Executive"},
    {"id": 503, "name": "Samay", "department": "R&D", "designation": "Intern"},
    {"id": 504, "name": "Samar", "department": "Marketing", "designation": "Digital Marketing"},
    {"id": 505, "name": "Arpit", "department": "IT", "designation": " Designer"},
]

def home(request):
  
    return render(request, 'home.html')

def employee_list(request):
    
    context = {
        'employees': EMPLOYEES
    }
    return render(request, 'employee_list.html', context)

def employee_detail(request, emp_id):
   
   
    employee = next((emp for emp in EMPLOYEES if emp['id'] == emp_id), None)
    
    context = {
        'employee': employee,
        'emp_id': emp_id
    }
    return render(request, 'employee_detail.html', context)

def about(request):
    return render(request, 'about.html')