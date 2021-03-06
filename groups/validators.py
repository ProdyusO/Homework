import datetime

from django.core.exceptions import ValidationError


def adult_validation(birthday):
    ADULT_AGE_LIMIT = 18

    age = datetime.datetime.now().year - birthday.year

    if age < ADULT_AGE_LIMIT:
        raise ValidationError('Age should be greater than 18')
