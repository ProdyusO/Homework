from django.db import models


class Person(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=80, null=False)
    city = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=120, null=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.city}, {self.email}'
