
from django.db import models

from faker import Faker

from core.models import Person


class Teacher(Person):
    phone_number = models.CharField(max_length=60, unique=True, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    @staticmethod
    def generate_teachers(*args):
        faker = Faker()
        for _ in range(*args):
            st = Teacher(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                phone_number=faker.phone_number(),
                city=faker.city(),
                email=faker.email(),
            )
            st.save()
