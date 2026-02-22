from rest_framework import serializers
from .models import Professional # Importa do Models, não dele mesmo!

class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = "__all__"