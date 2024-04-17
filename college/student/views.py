from django.shortcuts import render
from django.http import JsonResponse
from student.models import Student
import json

def student(request):
    if request.method == 'GET':
        students=Student.objects.all()
        student_data = []
        for student in students:
            student_data.append({
                "fisrt_name":student.first_name,
                "last_name":student.last_name,
                "roll_no":student.roll_no,
                'branch':student.branch,
                'birth_date':student.birthdate,
                "email":student.email,
                "phone_no":student.contact,
                'Year':student.year
            })
        return JsonResponse(student_data, safe=False)
    

    if request.method == 'POST':
        data = json.loads(request.body)
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        roll_no = data.get('roll_no')
        branch = data.get('branch')
        birthdate = data.get('birthdate')
        email = data.get('email')
        contact = data.get('contact')
        year = data.get('year')
        student= Student.objects.create(
            first_name = first_name ,
            last_name = last_name,
            roll_no = roll_no,
            branch = branch,
            birthdate = birthdate,
            email = email,
            contact = contact,
            year = year
        )
        return JsonResponse({'message': 'Student Data Created Succesfull' })
    

    if request.method == 'PUT':
        data = json.loads(request.body)
        student_id = data.get('student_id')
        try:
            student = Student.objects.get(id=student_id)


            student.first_name = data.get('first_name', student.first_name)
            student.last_name = data.get('last_name', student.last_name)
            student.roll_no = data.get('roll_no', student.roll_no)
            student.branch = data.get('branch', student.branch)
            student.birthdate = data.get('birthdate', student.birthdate)
            student.email = data.get('email', student.email)
            student.contact = data.get('contact', student.contact)
            student.year = data.get('year', student.year)
            


            student.save()
            return JsonResponse({
                'message': 'Student Data Update Succesfull'
            })
        
        except Student.DoesNotExist:
            return JsonResponse({
                'message': 'Student ID Does Not Exist'
             })







