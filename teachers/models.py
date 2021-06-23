from django.db import models

from faker import Faker


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=80, null=False)
    phone_number = models.CharField(max_length=60, unique=True, blank=True, null=False)
    city = models.CharField(max_length=65, null=False)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.phone_number}, {self.city}'

    @staticmethod
    def generate_teachers(*args):
        faker = Faker()
        for _ in range(*args):
            st = Teacher(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                phone_number=faker.phone_number(),
                city=faker.city(),
            )
            st.save()
