from django.db import models


class Course(models.Model):
    discipline = models.CharField(max_length=60, unique=True, blank=True, null=True)
    course = models.OneToOneField('groups.Group', on_delete=models.SET_NULL, null=True, related_name='number_course')

    def __str__(self):
        return f'{self.discipline}, {self.course}'
