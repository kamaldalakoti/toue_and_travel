from django.db import models
from django.urls import reverse
# Create your models here.
class Bus_list(models.Model):
    FROM = models.CharField(max_length=30)
    TO = models.CharField(max_length=30)
    PRICE = models.IntegerField()
    DATE = models.DateField()
    slug = models.SlugField(null=True)
    def __str__(self):
         return self.TO
    def get_absolute_url(self):
        return reverse('Home:bus_detail', kwargs={'slug': self.slug}) 
    
class Tour(models.Model):
    City = models.CharField(max_length=50)
    To = models.ForeignKey(Bus_list, on_delete=models.CASCADE,)   
    # img = models.ImageField(upload_to=None, height_field=200, width_field=200, max_length=None)
    img = models.FileField() 
    package = models.IntegerField()
    desc = models.TextField()
    slug = models.SlugField(null=True)
    duration = models.IntegerField(null=True)
    no_peaple = models.IntegerField(null=True)
    food = models.BooleanField(default=True)
    local = models.TextField(null=True)
    
    def __str__(self):
        return self.City
    def get_absolute_url(self):
        return reverse('Home:holiday_detail', kwargs={'slug': self.slug}) 