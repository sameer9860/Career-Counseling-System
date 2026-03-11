from django.db import models


class StudentInput(models.Model):
    name = models.CharField(max_length=100)
    grades = models.IntegerField()
    interest = models.CharField(max_length=50)
    subject = models.CharField(max_length=100, blank=True)
    hobbies = models.TextField(blank=True)
    traits = models.TextField(blank=True)
    suggestion = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.suggestion}"

