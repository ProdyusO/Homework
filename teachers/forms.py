from django.core.exceptions import ValidationError
from django.forms import ModelForm


from teachers.models import Teacher


class TeacherBaseForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'phone_number', 'city']

    @staticmethod
    def normalize_phone_number(value):
        return ''.join(c for c in value if c.isdigit() or c == '+')

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if Teacher.objects.filter(phone_number=phone_number).exclude(id=self.instance.id).exists():
            raise ValidationError("Already exist")
        result = self.normalize_phone_number(phone_number)
        return result


class TeacherCreateForm(TeacherBaseForm):
    pass


class TeacherUpdateForm(TeacherBaseForm):
    class Meta(TeacherBaseForm.Meta):
        model = Teacher
        fields = ['first_name', 'last_name', 'phone_number', 'city']
