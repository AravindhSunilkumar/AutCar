from django.shortcuts import redirect, render
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import user_details,services,UserBooking,BookingOrders
# Create your views here.

def index(request):
    return render(request, 'index.html')

def UserRegister(request):
    return render(request, 'User/User_register.html')


def user_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phoneno']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        
        data = user_details.objects.filter(username=username)
        if data.exists():
            messages.error(request, 'User already exists')
            return redirect(UserRegister)  
        
        if password == cpassword:
            user = user_details(name=name, email=email, phone_no=phone, username=username,password=password)
            user.save()
            return render(request, 'user/User_login.html')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect(UserRegister)  
            
    return redirect(UserRegister) 

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            data = user_details.objects.get(username = username)
            if password == data.password:
                request.session['user'] = username
                return redirect(UserHome)
            else:
                messages.error(request,'Invalid Password')
                return redirect(user_login)
        except Exception:
            messages.error(request,"Username not found")
            return redirect(user_login)
    return render(request,'user/user_login.html')       

def UserHome(request):
    return render(request,'user/UserHome.html',{'user':request.session['user']})

def ServiceListing(request):
    data = services.objects.all()
    return render(request,'user/ServiceListing.html',{'user':request.session['user'],'data':data})

def UserServices(request):
   
    return render(request,'user/UserServices.html',{'user':request.session['user']})

def Userbooking(request, i):
    user = user_details.objects.get(username=request.session['user'])
    data = services.objects.get(pk=i)
    datas = services.objects.all()
    time_slots = list(range(9, 22))  # 9 to 21 inclusive
    context = {
        'user': request.session['user'],
        'service': data.service_name,
        'services': datas,
        'data': data
    }
    return render(request, 'user/UserBooking.html', context)
    
    

def logout(request):
    if 'user' in request.session:
        request.session.flush()
        return redirect(index)
    return redirect(index)

def timeslotbooking(request): 
    if request.method == 'POST':
        # Get the selected services as a list of values
        user = user_details.objects.get(username=request.session['user'])
        selected_services = request.POST.getlist('services')
        s = ','.join(selected_services)
        print(s)
        
        
        # Get the other form fields
        service_date_str = request.POST.get('service_date')
        service_date = datetime.strptime(service_date_str, '%Y-%m-%d').date()
        car_model = request.POST.get('car_model')
        car_number = request.POST.get('car_number')
        print(service_date)
        
        # Debugging: Check the type of UserBooking
        print("UserBooking type:", type(UserBooking))
        
        # Logic to check booked time slots for the selected date
        booked_slots = UserBooking.objects.filter(date=service_date).values_list('time_slot', flat=True)
        
        # Generate all possible time slots (9 AM to 10 PM)
        all_time_slots = [f"{hour:02}:00" for hour in range(9, 22)]
        available_time_slots = [slot for slot in all_time_slots if slot not in booked_slots]
        print(available_time_slots)
        context = {
            'available_time_slots': available_time_slots,
            'user':user,
            'selected_services':s.strip(),
            'car_number':car_number,
            'car_model':car_model,
            'service_date':service_date
            
        }
    
    return render(request, 'user/TimeSlot.html',context)

# def order(request):
#     if request.method == 'POST':
#         user_details = user_details.objects.get(username = request.session['user'])
#         services = request.POST['services']
#         car_model = request.POST['car_model']
#         car_number = request.POST['car_number']
#         date = request.POST['date']
#         timslot = request.POST['timeSlot']
#         BookingOrders.objects.create(user=user_details,services = services,car_model = car_model,car_number = car_number,date = date,timslot = timslot)
        
        


# # Serv_Booking/views.py

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# from .models import UserBooking  # Adjust the import based on your app structure

# @csrf_exempt  # Only for development; handle CSRF correctly in production
# def get_available_time_slots(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         selected_date = data.get('date')

#         # Logic to check booked time slots for the selected date
#         booked_slots = UserBooking.objects.filter(date=selected_date).values_list('time_slot', flat=True)
        
#         # Generate all possible time slots (9 AM to 10 PM)
#         all_time_slots = [f"{hour:02}:00" for hour in range(9, 22)]
#         available_time_slots = [slot for slot in all_time_slots if slot not in booked_slots]

#         return JsonResponse({'available_time_slots': available_time_slots})

#     return JsonResponse({'error': 'Invalid request'}, status=400)

        
