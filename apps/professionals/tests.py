from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Professional

class ProfessionalTests(APITestCase):
    def test_create_professional(self):
        """Teste para criar um novo profissional"""
        # Ajustado para o padrão do Router do DRF
        url = reverse('professional-list') 
        data = {
            "social_name": "Felipe Silva",
            "profession": "Desenvolvedor",
            "address": "Rua Python, 123",
            "contact": "11999999999"
        }
        response = self.client.post(url, data, format='json')
        
        # Verificações
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Professional.objects.count(), 1)
        self.assertEqual(Professional.objects.get().social_name, "Felipe Silva")