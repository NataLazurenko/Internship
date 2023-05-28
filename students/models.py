from django.db import models


class Student(models.Model):
    id_user = models.IntegerField()
    age = models.TextField()
    city = models.TextField()
    university = models.TextField()
    direction = models.TextField()
    work_experience = models.TextField()
    internship_direction = models.TextField()