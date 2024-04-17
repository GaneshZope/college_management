from django.shortcuts import render
from django.http import JsonResponse
from student.models import Student


def student(request):
    if request.method == 'GET':
        students=Student.objects.all()
        student_data = []
        for student in students:
            student_data.append({
                "fisrt_name":student.first_name,
                "last_name":student.last_name,
                "roll no":student.roll_no,
                'branch':student.branch,
                'birth_date':student.birthdate,
                "email":student.email,
                "phone_no":student.contact,
                'Year':student.year
            })
        return JsonResponse(student_data, safe=False)

