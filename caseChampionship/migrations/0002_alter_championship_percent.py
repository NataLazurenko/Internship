# Generated by Django 3.2 on 2023-05-27 20:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caseChampionship', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='championship',
            name='percent',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]