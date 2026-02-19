from django.db import models

from apps.professionals.models import Professional

class Appointment(models.Model):
    date = models.DateTimeField()
    professional = models.ForeignKey(
        Professional,
        on_delete=models.CASCADE,
        related_name="appointments"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment - {self.professional.social_name}"
    
    class Meta:
        app_label = 'appointments'