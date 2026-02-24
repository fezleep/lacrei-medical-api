from rest_framework import serializers
from .models import Professional # Importa do Models, não dele mesmo!
from django.utils import timezone


class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = "__all__"

    def validate_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("A data da consulta não pode ser no passado.")
        return value