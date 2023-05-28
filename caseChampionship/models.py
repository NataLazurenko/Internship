from django.core import validators
from django.db import models
from main.models import Applications


class Championship(models.Model):
    application = models.ForeignKey(Applications, on_delete=models.CASCADE)
    percent = models.IntegerField(validators=[
        validators.MinValueValidator(0),
        validators.MaxValueValidator(100)
    ], null=True, blank=True)
    file = models.FileField(upload_to='championship/')
    created = models.DateTimeField(auto_now_add=True)