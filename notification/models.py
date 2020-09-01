from django.db import models

# Create your models here.
class Notification(models.Model):


   def __str__(self):
        return self.title