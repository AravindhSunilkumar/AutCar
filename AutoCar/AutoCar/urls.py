"""
URL configuration for AutoCar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Serv_Booking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index', views.index),
    path('UserRegister',views.UserRegister),
    path('user_register',views.user_register),
    path('user_login',views.user_login),
    path('UserHome',views.UserHome),
    path('ServiceListing',views.ServiceListing),
    path('UserServices',views.UserServices),
    path('UserBooking/<int:i>',views.UserBooking),
    path('sample/', views.sample, name='sample'),  # Your main page view
    # path('sample/process_date/', views.process_date, name='process_date'),
    path('get-time-slots/', views.get_available_time_slots, name='get_time_slots'),
    path('logout',views.logout),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)