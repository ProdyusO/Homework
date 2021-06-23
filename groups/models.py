import datetime

from django.db import models

from faker import Faker

from groups.validators import adult_validation


class Group(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=80, null=False)
    city = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=70, unique=True, blank=True, null=False)
    email = models.EmailField(max_length=120, null=True)
    birthday = models.DateField(default=datetime.date.today, validators=[adult_validation])

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.city}, {self.phone_number}, {self.email}, {self.birthday}'

    @staticmethod
    def generate_groups(count):
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
