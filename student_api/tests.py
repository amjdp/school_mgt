from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.
class TestSample(TestCase):

    def setup(self):
        self.client = APIClient  # To get url inbuilt

    def test_index(self):
        url = reverse('index')   
        # To get url pattern using name attribute('index')..we get path pattern
        res = self.client.get(url)  
        # To get response from the corresponding url (here response will be 'Congratulations... you have created an API')
        # Here res.data contains 'Congratulations... you have created an API'
        self.assertEquals(res.data,'Congratulations... you have created an API') 
        # assertEquals method compare 2 strings...... res.data-return value

    def test_number(self):
        url = reverse('number')
        res = self.client.get(url)
        self.assertEqual(res.data,10)
       