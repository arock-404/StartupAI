from django.db import models

# Create your models here.
class Entrepreneur(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    expertise = models.CharField(max_length=200)
    image = models.URLField()
    industry = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.company}"