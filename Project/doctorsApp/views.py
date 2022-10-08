import re
from django.shortcuts import render,redirect
from unicodedata import name
from django.shortcuts import render
from .forms import InformationForm, PatientForm, PrescriptionForm
from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth.forms import AuthenticationForm 
from doctorsApp.models import PatientDetails
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def home(request):
    my_dict={'var1': 'Welcome! Add Your Prescription',
                'var2': 'Home',
                'var3': '',
                'var4':'',
                'var8':'',
                'var5':'Sign Up',
                'var6':'Login',
                'var9': ''}
    return render(request,'home.html', context=my_dict)

def registerUser(request):
    if request.method == "POST":
        form = InformationForm(request.POST)
        if form.is_valid():
            print("Here")
            form.save()
            user=form.save()
            login(request, user)
            my_dict={'var1': "Welcome to the Dashboard "+form.cleaned_data.get('username'),
            'var2': '',
            'var3': 'View Patients',
            'var4':  'Add Prescription',
            'var8':'View Prescription ',
            'var5':' ',
            'var6':'Logout'}
            return render(request, 'home.html', context=my_dict)
    else:
        form = InformationForm()
    return render (request=request, template_name="registerPage.html", context={"register_form":form})


def loginUser(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                my_dict={'var1': "Welcome to the Dashboard "+form.cleaned_data.get('username'),
            'var3': 'View Patients',
            'var4':  'Add Prescription',
            'var8':'View Prescription  ',
            'var5':' ',
            'var6':'Logout'}
                return render(request, 'home.html', context=my_dict)
    else:
        form = AuthenticationForm()
    return render(request=request, template_name="loginPage.html", context={"login_form":form})

def logoutPage(request):
    logout(request)
    return redirect("/login/")

def patientDetails(request):
    if request.method == 'POST':
        form=PatientForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            age=form.cleaned_data['age']
            gender=form.cleaned_data['gender']
            email=form.cleaned_data['email']
            mobile=form.cleaned_data['mobile']
            address=form.cleaned_data['address']
            date=form.cleaned_data['date']
            symptoms=form.cleaned_data['symptoms']
            diagnosis=form.cleaned_data['diagnosis']

            patientInfo=PatientDetails(name=name, age=age,gender=gender, email= email, mobile=mobile, 
                                date=date, address=address, symptoms=symptoms,diagnosis=diagnosis)
            patientInfo.save()
            details={'name':name, 'age':age,'gender':gender, 'email':email, 'mobile':mobile, 
                               'address':address,'date':date,'symptoms':symptoms,'diagnosis':diagnosis}
            return render(request,'prescription.html',details)
    else:
        form=PatientForm()
    return render(request,'patientDetails.html',{'form':form})

def patientsList(request):
    if PatientDetails.objects.all().exists():
        patients=PatientDetails.objects.all()
        return render(request,'patientsList.html',context={'patient_entries':patients})
    else:
        return render(request,'patientsList.html',{'message':'No Patients Consulted Yet'})

def viewPrescription(request):
    if request.method == 'POST':
        form=PrescriptionForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            mobile=form.cleaned_data['mobile']
            if PatientDetails.objects.filter(mobile=mobile).exists():
                for i in PatientDetails.objects.filter(mobile=mobile):
                    if i.name==name:
                        details={'name':i.name, 'age':i.age,'gender':i.gender, 'email':i.email, 'mobile':mobile, 
                                'address':i.address, 'date':i.date, 'symptoms':i.symptoms,'diagnosis':i.diagnosis}
                        return render(request,'prescription.html',details)
                    else:
                       return render(request,'prescriptionForm.html',{'form':form, 'message':'Please Enter the Right Details'})
            else:
                return render(request,'prescriptionForm.html',{'form':form, 'message':'Please Enter the Right Details'})
                
        else:
            return render(request,'prescriptionForm.html',{'form':form, 'message':'Please Enter the Right Details'})
    
    else:
        form=PrescriptionForm()
    return render(request,'prescriptionForm.html',{'form':form})
    