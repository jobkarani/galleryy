import cloudinary
from django.db import models
from datetime import date 
from cloudinary.models import CloudinaryField
# Create your models here.
# location
class Location(models.Model):
    name = models.CharField(max_length =30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name


# category
class Category(models.Model):
    name = models.CharField(max_length =30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name


# image
class Image(models.Model):
    name = models.CharField(max_length =30)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.PROTECT, blank =True )
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image = CloudinaryField('image')
    posted_on = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self,name,location,category):
        self.name = name
        self.location = location
        self.category = category
        self.save()

    @classmethod
    def get_image_by_id(cls, id):
        img = Image.objects.get(id=id)
        return img

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__name__icontains=search_term)
        return images
        
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']