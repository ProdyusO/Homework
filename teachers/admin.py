from django.contrib import admin

from .models import Teacher
from groups.models import Group


class CourseInLineTable(admin.TabularInline):
     model = Group
     fields = [
         ('first_name', 'last_name'),
         ('city', 'email'),
         'teacher'
     ]


     show_change_link = True
     extra = 0

# поключаем класс, который разделит поля во главной вьюхе приложения groups
class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'email',
        'phone_number',
    ]

    # Указываем какие поля будут линками в данном случа все вышеуказанные
    list_display_links = list_display

# вывод количества обьектов на одной странице
    list_per_page = 5

# Отображает по блокам страницу с апргрейдом студента в группе
    fields = [
        ('first_name', 'last_name'),
        ('email', 'phone_number'),
        'city'
    ]

# Убирает редактирующее поле
    # readonly_fields = ['birthday']

# Поля по которым будут происходить поиск. В данном случае по имени и фамилии
    search_fields = ['first_name', 'last_name']

# Добовляет фильтр панель справа
    #list_filter = ['phone_number']

    inlines = [CourseInLineTable]


# Зарегистрировать в панели администратора приложение  groups и подключить вышепрописанную модель GroupAdmin
admin.site.register(Teacher, TeacherAdmin)
