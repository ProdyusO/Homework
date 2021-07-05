from django.urls import path

from courses.views import get_course, create_course, update_course, delete_course

app_name = 'courses'

urlpatterns = [
    path('', get_course, name='list'),
    path('create/', create_course, name='create'),
    path('update/<int:pk>/', update_course, name='update'),
    path('delete/<int:pk>/', delete_course, name='delete'),
]