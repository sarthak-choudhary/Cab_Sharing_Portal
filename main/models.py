from django.db import models
from django.contrib.auth.models import User

# Create your models here.
LOCATION_CHOICES = [
    ('IGI','DELHI AIRPORT'),
    ('PIL','PILANI'),
    ('LOH','LOHARU'),
    ('NDL','New Delhi Railway Station'),
    ('JAI','Jaipur Airport'),
]

class Cab(models.Model):
    id = models.IntegerField(primary_key=True)
    time_of_dep = models.TimeField(auto_now=False)

class passengers(models.Model):
    passenger = models.ForeignKey(User,on_delete=models.CASCADE,related_name='passenger')
    no_of_seats = models.PositiveSmallIntegerField()
    from_location = models.CharField(max_length=3,choices=LOCATION_CHOICES)
    to_location = models.CharField(max_length=3, choices=LOCATION_CHOICES)
    starting_time = models.TimeField(auto_now=False)
    date = models.DateField(auto_now=False)
    cab = models.ForeignKey(to=Cab,related_name='passengers',null=True,blank=True,on_delete=models.SET_NULL)
