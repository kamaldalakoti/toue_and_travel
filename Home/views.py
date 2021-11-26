from django.shortcuts import render,redirect,get_object_or_404
from Home.models import Bus_list , Tour

# Create your views here.
def Home(request):
    if request.method == "POST":
        From_data = request.POST.get('From')
        To_data = request.POST.get('To')
        
        bus_list = Bus_list.objects.all().filter(FROM = From_data , TO = To_data )
        # if bus_list is not None :
        # else:
        # Data = {'From1': ' No buss for '  ,'TOO':To_data , 'Fromm':From_data }
        
        Tour_plan = Tour.objects.all().filter(City=To_data)  
        # City_name = Tour.objects.get(City=To_data)  
        Data = {'From':bus_list ,'TOO':To_data , 'Fromm':From_data , 'Tour_plan1': Tour_plan }   
            
        
        
        return render(request, 'index.html',Data )
    return render(request, 'index.html' ) 
def contact(request):
    return render(request, 'contact.html')
def about (request):
    return render(request, 'about.html')
def Holidays_package(request):
    if request.method == 'POST':
        QRY = request.POST.get('qry')
        Tour_plan = Tour.objects.all().filter(City=QRY)
        Data = {'Tour_plan1': Tour_plan}
        # print(QRY)
        return render(request, 'holiday.html', Data)
    return render(request, 'holiday.html', )
def bus_detail(request , slug):
    # item = get_object_or_404(Bus_list, slug)
    bus_list = Bus_list.objects.filter(slug = slug)
    # print(bus_list)
    data = {'bust_list': bus_list}
        
    return render(request, 'bus_detail.html',data )
def holiday_detail(request , slug):
    # item = get_object_or_404(Bus_list, slug)
    bus_list = Tour.objects.filter(slug = slug)
    # print(bus_list)
    data = {'bust_list': bus_list}
        
    return render(request, 'holiday_detail.html', data)
