from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Category, Auto

User = get_user_model()

class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='12345')
        self.category = Category.objects.create(name='Test Category')
        self.auto = Auto.objects.create(
            category=self.category,
            mark='Test Mark',
            model='Test Model',
            type_of_body='SEDAN',
            transmission='AUTOMAT',
            wheel='LEFT',
            color='BLACK',
            location='Test Location',
            price=10000,
            ranting='FROM 6 TO 24 HOURS',
            body='Test Content',
            number='1234567890',
            user=self.user
        )

    def test_category_creation(self):
        category = Category.objects.get(name='Test Category')
        self.assertEqual(category.name, 'Test Category')

    def test_auto_creation(self):
        auto = Auto.objects.get(mark='Test Mark')
        self.assertEqual(auto.model, 'Test Model')
        self.assertEqual(auto.type_of_body, 'SEDAN')
        self.assertEqual(auto.transmission, 'AUTOMAT')
        self.assertEqual(auto.wheel, 'LEFT')
        self.assertEqual(auto.color, 'BLACK')
        self.assertEqual(auto.location, 'Test Location')
        self.assertEqual(auto.price, 10000)
        self.assertEqual(auto.ranting, 'FROM 6 TO 24 HOURS')
        self.assertEqual(auto.body, 'Test Content')
        self.assertEqual(auto.number, '1234567890')
        self.assertEqual(auto.user, self.user)
