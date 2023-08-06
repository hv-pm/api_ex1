from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_metrics(value):
    if value < 0:
        raise ValidationError(
            _("This field can not accept numbers below 0."),
            params={'value': value},
        )


class Rocket(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=100)
    height = models.IntegerField(validators=[validate_metrics])
    diameter = models.IntegerField(validators=[validate_metrics])
    mass = models.IntegerField(validators=[validate_metrics])
    image = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
