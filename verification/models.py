from django.db import models
from applications.models import Application

class Attendance(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    proof_image = models.ImageField(upload_to="proofs/")
    check_in_time = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
