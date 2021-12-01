from django.test import TestCase
from .models import Location,Category,Image

# Create your tests here.
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        """creation of location for testing
        """
        Location.objects.create(name="nairobi")

    
    def test_location_name(self):
        """tests the location name
        """
        location=Location.objects.get(name="nairobi")
        self.assertEqual(location.name, "nairobi")
        
    def test_location_str(self):
        """checks if the locations string is right
        """
        location=Location.objects.get(name="nairobi")
        self.assertEqual(str(location), "nairobi")
        
class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        """creation of category for testing
        """
        Category.objects.create(name="art")

    
    def test_category_name(self):
        """tests the category name
        """
        category=Category.objects.get(name="art")
        self.assertEqual(category.name, "art")
        
    def test_category_str(self):
        """checks if the category string is right
        """
        category=Category.objects.get(name="art")
        self.assertEqual(str(category), "art")
        
class ImageTestCase(TestCase):
    def setUp(self):
        """image creation
        """
        Image.objects.create(
            name="init",
            description="hey",
            location=Location.objects.create(name="nairobi"),
            category=Category.objects.create(name="art"),
        )
    def test_image_name(self):
        """tests image name
        """
        image=Image.objects.get(name="init")
        self.assertEqual(image.name, "init")
        
    def test_image_description(self):
        """tests image description
        """
        image=Image.objects.get(name="init")
        self.assertEqual(image.description, "hey")
        
    def test_image_category(self):
        """tests image category
        """
        image=Image.objects.get(name="init")
        self.assertEqual(image.category.name, "art")
        
    def test_image_location(self):
        """tests image location
        """
        image=Image.objects.get(name="init")
        self.assertEqual(image.location.name, "nairobi")
        
    def test_image_str(self):
        """checks if the image string is right
        """
        image=Image.objects.get(name="init")
        self.assertEqual(str(image), "init")