import json
from .models import Student
from django.conf import settings
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_student(request):
    if request.method == "POST":
        student = Student(student_name=request.POST['name'], student_age=request.POST['age'],
                          student_address=request.POST['address'], student_image=request.FILES['image'])
        student.save()
        return JsonResponse({"message": "Record saved successfully"})


def get_all_students(request):
    student = Student.objects.all().values()
    return JsonResponse({"students": list(student)}, safe=False)


def get_student_by_id(request, id=1):
    student = Student.objects.filter(student_id=id).values()
    return JsonResponse({"student": list(student)}, safe=False)


@csrf_exempt
def update_student_by_id(request, id):
    if request.method == 'PATCH':
        requested_json_data = json.loads(request.body.decode('utf-8'))
        Student.objects.filter(student_id=id).update(student_name=requested_json_data['name'],
                                                     student_age=requested_json_data['age'], student_address=
                                                     requested_json_data['address'])
        return JsonResponse({"message": "Record updated successfully"})


@csrf_exempt
def delete_student_by_id(request, id):
    if request.method == "DELETE":
        Student.objects.filter(student_id=id).delete()
        return JsonResponse({"message": "Record deleted successfully"})


@csrf_exempt
def send_student_enquiry_mail(request):
    if request.method == "POST":
        message = "Message from: " + request.POST['name'] + '\n' + "Email: " + request.POST['email'] + '\n' + "" \
                    "Phone: " + request.POST['phone'] + "\n" + "Subject: " + request.POST['subject'] + '\n' + "" \
                    "message: " + request.POST['message']

        mail = EmailMessage("Student Enquiry", message, settings.EMAIL_HOST_USER, ["abhishek.padghane@infimetrics.com",
                                                                                   "tdeshmukh1993@gmail.com"])

        for attachment in request.FILES.getlist('attachment'):
            mail.attach(attachment.name, attachment.read(), attachment.content_type)

        mail.send()
        return JsonResponse({"message": "Enquiry sent successfully"})
