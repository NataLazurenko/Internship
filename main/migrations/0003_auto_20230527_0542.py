# Generated by Django 3.2 on 2023-05-27 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_applications_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applications',
            name='user',
        ),
        migrations.AddField(
            model_name='applications',
            name='full_name',
            field=models.CharField(default='ФИО', max_length=200),
        ),
    ]
