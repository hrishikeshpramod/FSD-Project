from email.policy import default
from django.db import models
from crispy_forms.layout import Layout,Submit
from crispy_forms.layout import Column
from crispy_forms.layout import Row
from crispy_forms.helper import FormHelper

# Create your models here.
class PatientDetails(models.Model):
    name=models.CharField(max_length=50, default='')
    age=models.IntegerField(default=1)
    gender=models.CharField(max_length=50, default='')
    email=models.EmailField()
    mobile=models.CharField(max_length=50, default='')
    address=models.CharField(max_length=50, default='')
    date=models.DateField()

    symptoms=models.CharField(max_length=150, default='')
    diagnosis=models.CharField(max_length=150, default='')
    
    def __str__(self):
        return self.name + self.mobile