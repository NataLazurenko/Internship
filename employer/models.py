from django.db import models

class RequestInternModel(models.Model):
    age = models.TextField()
    city = models.TextField()
    university = models.TextField()
    direction = models.TextField()
    work_experience = models.TextField()
    internship_direction = models.TextField()
    id_tutor = models.TextField()


# Create your models here.
