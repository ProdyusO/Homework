from courses.models import Course

from django.forms import ModelForm


class CourseBaseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        exclude = ['course']


class CourseCreateForm(CourseBaseForm):
    pass


class CourseUpdateForm(CourseBaseForm):
    pass


class CourseDeleteForm(CourseBaseForm):
    pass
