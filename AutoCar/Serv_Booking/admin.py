from django.contrib import admin
from .models import user_details,services,services_cart,UserBooking
# Register your models here.
admin.site.register(user_details)
admin.site.register(services)
admin.site.register(services_cart)
admin.site.register(UserBooking)
