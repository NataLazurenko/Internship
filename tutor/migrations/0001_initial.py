# Generated by Django 4.2 on 2023-05-27 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SetMentorToStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_mentor', models.IntegerField()),
                ('id_student', models.IntegerField()),
            ],
        ),
    ]