from django.contrib import admin
from .models import user_details,services,UserBooking,BookingOrders
# Register your models here.
admin.site.register(user_details)
admin.site.register(services)
admin.site.register(BookingOrders)

admin.site.register(UserBooking)
