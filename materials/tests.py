from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Course, Lesson, Subscription

User = get_user_model()

class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='testpass')
        self.course = Course.objects.create(title='Test Course', description='Test Description')
        self.client.force_authenticate(user=self.user)

    def test_subscribe(self):
        url = '/api/subscribe/'
        data = {'course_id': self.course.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Subscription.objects.count(), 1)

    def test_unsubscribe(self):
        Subscription.objects.create(user=self.user, course=self.course)
        url = '/api/subscribe/'
        data = {'course_id': self.course.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Subscription.objects.count(), 0)
