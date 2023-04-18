from django.db import models

from .validators import validate_year


class Car(models.Model):

    name = models.CharField(
        verbose_name='Название авто',
        max_length=300,
    )
    year = models.IntegerField(
        verbose_name='Год выпуска',
        validators=[validate_year],
    )

    class Meta:
        ordering = ['-year']


class CarImage(models.Model):

    photo = models.ImageField(
        verbose_name='Фото автомобиля',
        upload_to='photos/',
        default='photos/default.jpg',
        blank=True, null=True,
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.SET_DEFAULT,
        default='photos/default.jpg',
        blank=True,
        null=True,
        related_name='images',
    )

