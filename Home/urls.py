from django.contrib import admin
from django.urls import path
from Home import views
app_name = 'Home'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.Home),
    path('/',views.Home),
    path('Holidays',views.Holidays_package),
    path('contact',views.contact),
    path('about',views.about),
    path('<slug>/bus_detail',views.bus_detail,name='bus_detail' ),
    path('<slug>/holiday_detail',views.holiday_detail,name='holiday_detail' )
]