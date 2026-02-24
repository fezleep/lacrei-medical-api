from rest_framework import serializers
from .models import Appointment
from django.utils import timezone

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"

    def validate_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("A data da consulta não pode ser no passado.")
        return value