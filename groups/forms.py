import django_filters
from django.core.exceptions import ValidationError
from django.forms import DateInput, ModelForm

from groups.models import Group


class GroupBaseForm(ModelForm):
    class Meta:
        model = Group
        fields = ['first_name', 'last_name', 'city', 'phone_number', 'birthday', 'email']
        widgets = {
            'birthday': DateInput(attrs={'type': 'date'})
            }

    @staticmethod
    def normalize_name(value):
        return value.lower().capitalize()

    @staticmethod
    def normalize_phone_number(value):
        return ''.join(c for c in value if c.isdigit() or c == '+')

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        result = self.normalize_name(first_name)
        return result

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        result = self.normalize_name(last_name)
        return result

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if Group.objects.filter(phone_number=phone_number).exclude(id=self.instance.id).exists():
            raise ValidationError("Already exist")
        result = self.normalize_phone_number(phone_number)
        return result


class GroupCreateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        model = Group
        # fields = ['first_name', 'last_name', 'city', 'phone_number', 'birthday', 'email']
        fields = '__all__'


class GroupUpdateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        model = Group
        #fields = ['first_name', 'last_name', 'city', 'phone_number', 'birthday', 'email']
        fields = '__all__'


class GroupsFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
        }
