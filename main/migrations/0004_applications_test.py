# Generated by Django 3.2 on 2023-05-27 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20230527_0542'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='test',
            field=models.BooleanField(default=False),
        ),
    ]
