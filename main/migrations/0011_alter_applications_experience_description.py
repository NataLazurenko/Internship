# Generated by Django 4.2.1 on 2023-05-27 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_applications_experience_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='experience_description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
