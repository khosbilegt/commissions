from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    isadmin = models.BooleanField(null = True, blank = True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'users'

class Room(models.Model):
    room_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    rooms = models.IntegerField(null=True, blank=True)
    beds = models.IntegerField(null=True, blank=True)
    bathrooms = models.IntegerField(null=True, blank=True)
    balconies = models.IntegerField(null=True, blank=True)
    adults = models.IntegerField(null=True, blank=True)
    children = models.IntegerField(null=True, blank=True)
    haswifi = models.BooleanField(null=True, blank=True)
    hastv = models.BooleanField(null=True, blank=True)
    hasminibar = models.BooleanField(null=True, blank=True) 
    hasac = models.BooleanField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    
    class Meta:
       db_table = 'rooms'