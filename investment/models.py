from django.db import models
from django.conf import settings

class Investment(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    investment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    participation_porcentage = models.DecimalField(max_digits=5, decimal_places=2)
    wallet = models.CharField(max_length=255)

    def __str__(self):
        return str(self.user) + ' - ' + str(self.amount)