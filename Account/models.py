# models.py
from django.db import models

class Payment(models.Model):
    member = models.CharField(max_length=255)
    month= models.CharField(max_length=3,null=True)
    year= models.IntegerField(default=1000)
    value=models.IntegerField(default=0)
    def __str__(self):
        return self.member
