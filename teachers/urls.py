from django.urls import path
# from teachers.views import create_teacher, delete_teacher, get_teachers, update_teacher

from .views import TeacherCreateView, TeacherDeleteView, TeacherListView, TeacherUpdateView
app_name = 'teachers'

urlpatterns = [
    path('', TeacherListView. as_view(), name='list'),
    path('create', TeacherCreateView.as_view(), name='create'),
    path('update/<int:pk>', TeacherUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', TeacherDeleteView.as_view(), name='delete'),
]
