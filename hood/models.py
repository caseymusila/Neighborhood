from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from cloudinary.models import CloudinaryField

# Create your models here.
class Hood(models.Model):
    user = models.ForeignKey('Profile', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, null=True)
    description = models.CharField(max_length=400, null=True)
    location = models.CharField(max_length=200, null=True)
    population = models.IntegerField()
    image = CloudinaryField('image')

    def __str__(self):
        return self.name
    
    def create_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def find_hood(cls, id):
        hood = cls.objects.get(id = id)
        return hood

    def update_hood(self, name):
        self.name = name
        self.save()