from django.db import models

class SetMentorToStudent(models.Model):
    id_mentor = models.IntegerField()
    id_student = models.IntegerField()
    id_tutor = models.IntegerField()

# Create your models here.
