from django.db import models
from django.db.models.fields import DateField

class Car(models.Model):
    brand = models.CharField(max_length=50)
    hp = models.IntegerField()
    cc = models.IntegerField()
    type = models.CharField(max_length=20)
    year_made = DateField()

    def __str__(self):
        return self.brand
