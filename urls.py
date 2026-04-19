from django.urls import path
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # Path for the submit view
    path('<int:course_id>/submit/', views.submit, name='submit'),
    
    # Path for the show_exam_result view
    path('<int:course_id>/show_exam_result/', views.show_exam_result, name='show_exam_result'),
]
