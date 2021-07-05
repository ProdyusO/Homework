from courses.models import Course
from django.forms import ModelForm


class CourseBaseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        exclude = ['course']

class CourseCreateForm(CourseBaseForm):
    class Meta(CourseBaseForm.Meta):
        model = Course
        fields = '__all__'



class CourseUpdateForm(CourseBaseForm):
    class Meta(CourseBaseForm.Meta):
        model = Course
        fields = '__all__'
