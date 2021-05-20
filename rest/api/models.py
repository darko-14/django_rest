from django.db import models
from django.db.models.fields import DateTimeField

class Member(models.Model):

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(max_length=40)
    member_since = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
