import datetime

from django.core.exceptions import ValidationError


def validate_year(val):
    current_year = datetime.date.today().year
    if val > current_year or val < 1900:
        raise ValidationError(
            'Год должен быть меньше или равен текущему, но больше 1900.'
        )
