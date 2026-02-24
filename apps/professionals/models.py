from django.db import models


class Professional(models.Model):
    social_name = models.CharField(max_length=150)
    profession = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
            app_label = 'professionals' 

    def __str__(self):
        return self.social_name