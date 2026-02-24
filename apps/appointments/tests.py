from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# Estes dois imports abaixo são OBRIGATÓRIOS:
from apps.professionals.models import Professional
from apps.appointments.models import Appointment 

class AppointmentTests(APITestCase):
    def setUp(self):
        # Cria um profissional para poder vincular a consulta
        self.professional = Professional.objects.create(
            social_name="Dr. Teste",
            profession="Psicólogo",
            address="Rua Teste, 123",
            contact="11999999999"
        )
        self.list_url = reverse('appointment-list')

    def test_create_appointment(self):
        """Teste para criar uma nova consulta"""
        data = {
            "date": "2026-03-20T14:00:00Z",
            "professional": self.professional.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Agora o código vai saber o que é 'Appointment'
        self.assertEqual(Appointment.objects.count(), 1)

    def test_filter_appointments_by_professional(self):
        """Teste do requisito obrigatório: Buscar consultas por ID do profissional"""
        Appointment.objects.create(
            date="2026-03-20T14:00:00Z",
            professional=self.professional
        )
        
        url = f"/api/appointments/by-professional/{self.professional.id}/"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)