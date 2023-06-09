# Generated by Django 3.2 on 2023-05-27 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0011_alter_applications_experience_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applications',
            name='full_name',
        ),
        migrations.AddField(
            model_name='applications',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='applications',
            name='experience',
            field=models.CharField(choices=[('public activaty', 'Общественная деятельноеть'), ('voluneer', 'Волонтерская деятельноеть'), ('project activaty', 'Проектная деятельноеть'), ('other', 'Нет опыта работы')], max_length=200, null=True),
        ),
    ]
