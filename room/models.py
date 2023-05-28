from django.db import models

class Room(models.Model):
    id_mentor = models.IntegerField()
    id_student = models.IntegerField()
    text_task = models.TextField()
    task_links = models.TextField()

# Create your models here.
