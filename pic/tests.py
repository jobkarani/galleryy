from _typeshed import Self
from django.test import TestCase
from .models import Location,Category,Image

# Create your tests here.
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self,name):
        
        self.nairobi = Location(Self.nairobi,Location)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))