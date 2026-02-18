from django.db import models
from applications.models import Application

class Payment(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, default="pending")
    paid_at = models.DateTimeField(null=True, blank=True)
