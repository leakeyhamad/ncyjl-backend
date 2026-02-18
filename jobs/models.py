from django.db import models
from django.conf import settings

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    sub_county = models.CharField(max_length=100)
    vacancies = models.IntegerField()
    is_open = models.BooleanField(default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    required_skills = models.ManyToManyField(Skill)
    created_at = models.DateTimeField(auto_now_add=True)
