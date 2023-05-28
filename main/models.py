from django.conf import settings
from django.core import validators
from django.db import models
from django.contrib.auth.models import User


class Applications(models.Model):
    # законьчевший 3 курс бакалавра
    # 4 курс бакалавра
    # магистр
    # высшее образование
    class Education(models.TextChoices):
        RUSSIAN = 'completed 3rd year bachelor', 'Законьчевший 3 курс бакалавра'
        COMPUTER = 'completed 4 year bachelor', 'Законьчевший 4 курс бакалавра'
        MASTER = 'master', 'Магистер'
        HIGHER_EDUCATION = 'higher education', 'высшее образование'
        OTHER = 'other', 'Другое'

    class Experience(models.TextChoices):
        PUBLIC_ACTIVITY = 'public activaty', 'Общественная деятельноеть'
        VOLUNTEER = 'voluneer', 'Волонтерская деятельноеть'
        PROJECT_ACTIVITY = 'project activaty', 'Проектная деятельноеть'
        OTHER = 'other', 'Нет опыта работы'

    full_name = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    career = models.BooleanField(default=False)
    test = models.BooleanField(default=False)
    recommended = models.BooleanField(default=True)
    education = models.CharField(max_length=200, choices=Education.choices)
    russian_citizenship = models.BooleanField(default=True)
    age = models.IntegerField(validators=[
        validators.MinValueValidator(1),
        validators.MaxValueValidator(100)
    ])
    archive = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    career_percent = models.IntegerField(validators=[
        validators.MinValueValidator(1),
        validators.MaxValueValidator(100)
    ],
        null=True)
    experience = models.CharField(max_length=200, choices=Experience.choices, null=True)
    experience_description = models.TextField(max_length=1000, null=True, blank=True)

    def get_status(self):
        if self.test:
            return "Тестирование"
        elif not self.career:
            return "В обработке"
        elif self.career:
            return "Карьерная школа"



class ApplicationTest(models.Model):
    class Subjects(models.TextChoices):
        RUSSIAN = 'russian', 'Русский язык'
        COMPUTER = 'computer', 'Компьютерная граммотность'
        ANALYSIS = 'analysis', 'Анализ информации'

    application = models.ForeignKey(Applications, on_delete=models.CASCADE)
    subject = models.CharField(choices=Subjects.choices, max_length=200)
    value = models.IntegerField(validators=[
        validators.MinValueValidator(0),
        validators.MaxValueValidator(100)
    ])
    created = models.DateTimeField(auto_now_add=True, null=True)
