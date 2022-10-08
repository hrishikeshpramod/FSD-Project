import re
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
from crispy_forms.layout import Column
from crispy_forms.layout import Row
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class InformationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username",'first_name',"last_name", "email", "password1", "password2")
    
class PatientForm(forms.Form):
    name=forms.CharField(label='Name')
    age=forms.CharField(label='Age')
    gender=forms.CharField(label='Gender')
    email=forms.EmailField(label='Email')
    mobile=forms.CharField(label='Mobile')
    address=forms.CharField(label='Address')
    date=forms.DateField(label='Date', widget=forms.DateInput(attrs={'type':'date', 'max':datetime.now().date()}))

    symptoms=forms.CharField(label='Symptoms')
    diagnosis=forms.CharField(label='Diagnosis')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper=FormHelper(self)
        self.helper.form_class = ' container justify-content-center '
        self.helper.form_method="post"
        self.helper.layout=Layout(
			Row(
                Column('name', css_class='form-group col-md-4  mb-10'),
                Column('age', css_class='form-group col-md-4  mb-10'),
                Column('gender', css_class='form-group col-md-4 mb-10'),
                css_class='form-row  center'
            ),
            Row(
                Column('address', css_class='form-group col-md-6  mb-10'),
                Column('email', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('mobile', css_class='form-group col-md-6  mb-10'),
                Column('date', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
            'symptoms',
            'diagnosis',
			Submit('submit','Submit',css_class="btn-info")
			)

class PrescriptionForm(forms.Form):
    name=forms.CharField(label='Name')
    mobile=forms.CharField(label='Mobile')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper=FormHelper(self)
        self.helper.form_class = ' container justify-content-center '
        self.helper.form_method="post"
        self.helper.layout=Layout(
			'name',
            'mobile',
			Submit('submit','Submit',css_class="btn-info")
			)