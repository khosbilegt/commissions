from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    role = models.CharField(max_length=25)

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

class RoomBooking(models.Model):
    booking_id = models.UUIDField(default=uuid.uuid4, editable=False)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    customer_name = models.CharField(max_length=100)
    customer_number = models.CharField(max_length=15)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
       db_table = 'roombooking'

class Hall(models.Model):
    hall_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    description = models.TextField()
    chairsonly = models.IntegerField()
    roundtable = models.IntegerField()
    studenttable = models.IntegerField()
    pshape = models.IntegerField()
        
    class Meta:
       db_table = 'halls'

class HallBooking(models.Model):
    booking_id = models.UUIDField(default=uuid.uuid4, editable=False)
    hall_id = models.ForeignKey(Hall, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    customer_name = models.CharField(max_length=100)
    customer_number = models.CharField(max_length=15)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
        
    class Meta:
       db_table = 'hallbooking'