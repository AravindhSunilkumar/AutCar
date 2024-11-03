from django.db import models

# Create your models here.
class user_details(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_no = models.CharField(max_length=100)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class services(models.Model):
    service_name = models.CharField(max_length=255)
    service_discription = models.TextField(max_length=255)
    service_amount = models.FloatField()
    service_image = models.FileField()
    def __str__(self):
        return self.service_name


    
class UserBooking(models.Model):
    user = models.ForeignKey(user_details, on_delete=models.CASCADE, related_name='bookings')
    service = models.ForeignKey(services, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
    time_slot = models.CharField(max_length=15)  # e.g., "09:00" or "14:00"
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the booking was made

    def __str__(self):
        return f"Booking by {self.user.name} for {self.service.service_name} on {self.date} at {self.time_slot}"

class BookingOrders(models.Model):
    user = models.ForeignKey(user_details, on_delete=models.CASCADE)
    services = models.CharField(max_length=255)
    car_model = models.CharField(max_length=255)
    car_number = models.CharField(max_length=255)
    date = models.DateField()
    timslot =models.CharField(max_length= 255)
    payment_status =models.CharField(max_length=255, default='Pending') 
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Booking by {self.user.name} for {self.services} on {self.date} at {self.time_slot}"