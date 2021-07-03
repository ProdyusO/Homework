from django.db import models


class Course(models.Model):
    course = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.course}'

