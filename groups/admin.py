from django.contrib import admin

from .models import Group
from courses.models import Course


class CourseInLineTable(admin.TabularInline):
     model = Course
     fields = [
         'discipline'
     ]


     show_change_link = True
     extra = 0




# поключаем класс, который разделит поля во главной вьюхе приложения groups
class GroupAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'birthday',
        'phone_number',
    ]

    # Указываем какие поля будут линками в данном случа все вышеуказанные
    list_display_links = list_display

# вывод количества обьектов на одной странице
    list_per_page = 5

# Отображает по блокам страницу с апргрейдом студента в группе
    fields = [
        ('first_name', 'last_name'),
        ('birthday', 'city'),
        ('email', 'phone_number'),
        'teacher'
    ]

# Убирает редактирующее поле
    # readonly_fields = ['birthday']

# Поля по которым будут происходить поиск. В данном случае по имени и фамилии
    search_fields = ['first_name', 'last_name']

# Добовляет фильтр панель справа
    list_filter = ['phone_number']

    inlines = [CourseInLineTable]


# Зарегистрировать в панели администратора приложение  groups и подключить вышепрописанную модель GroupAdmin
admin.site.register(Group, GroupAdmin)
