from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse
from restaurant.serializers import menuSerializer
from django.http import JsonResponse
from rest_framework.response import Response
import json

class  MenuViewTest(TestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(title="Pizza", price=100.99, inventory=100)
        self.menu2 = Menu.objects.create(title="Pasta", price=800.99, inventory=14)
        self.menu3 = Menu.objects.create(title="Salad", price=500.99, inventory=51)

    

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))
        menus = Menu.objects.all()
        serialized_menus = menuSerializer(menus, many=True)
        serie = Response(serialized_menus.data)
        
        self.assertEqual(response.content.decode(), serie)