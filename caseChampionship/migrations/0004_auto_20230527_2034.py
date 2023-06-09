# Generated by Django 3.2 on 2023-05-27 20:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caseChampionship', '0003_alter_championship_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='championship',
            name='file',
            field=models.FileField(upload_to='championship/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['zip', 'tar gz', 'rar'])]),
        ),
        migrations.AlterField(
            model_name='championship',
            name='percent',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
