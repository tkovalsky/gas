from django.db import models

# Create your models here.
class Area(models.Model):
    area_name = models.CharField(max_length=200)
    date_added = models.DateTimeField('date added')

class Parcels(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    property_type
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    size
    measured_in = models.CharField(max_length=25)
    date_added = models.DateTimeField('date added')


class Owners(models.Model):
    owner_name = models.CharField(max_length=200)
    date_added = models.DateTimeField('date added')
