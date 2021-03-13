from django.urls import path
from .views import add_student, get_all_students, get_student_by_id, update_student_by_id, delete_student_by_id, \
                    send_student_enquiry_mail


urlpatterns = [
    path('add_student/', add_student),
    path('get_all_students/', get_all_students),
    path('get_student/<int:id>/', get_student_by_id),
    path('update_student/<int:id>/', update_student_by_id),
    path('delete_student/<int:id>/', delete_student_by_id),
    path('student_enquiry/', send_student_enquiry_mail),
]
