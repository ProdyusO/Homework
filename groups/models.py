import datetime

from django.db import models

from faker import Faker

from core.models import Person
from groups.validators import adult_validation
from teachers.models import Teacher


class Group(Person):
    phone_number = models.CharField(max_length=70, unique=True, blank=True, null=True)
    birthday = models.DateField(default=datetime.date.today, validators=[adult_validation])
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, related_name='students')
    course = models.OneToOneField('Courses.Course', on_delete=models.SET_NULL, null=True, related_name='number_course')

    def __str__(self):
        return f' {self.phone_number}, {self.birthday}, {self.teacher}, {self.course}'

    @staticmethod
    def generate_students(count):
        faker = Faker()
        for _ in range(count):
            st = Group(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                city=faker.city(),
                phone_number=faker.phone_number(),
                email=faker.email(),
            )
            st.save()
