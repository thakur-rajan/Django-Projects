from django import forms
from.models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

# Student Registration Form
class Registration(forms.ModelForm):
    
    class Meta:
        model=Student
        fields=['name','dob','address','phoneNumber','email','course','gender']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control' ,'type':'date'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'phoneNumber':forms.TextInput(attrs={'class':'form-control ',}),
            'email':forms.EmailInput(attrs={'class':'form-control','type':'email'}),
            'course':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.TextInput(attrs={'class':'form-control'})
            }  
        error_messages = {
              'name': {'required': 'Enter your name'},
              'dob': {'required': 'Enter Your Date of Birth'},
              'address': {'required': 'Enter Your Address'},
              'phoneNumber': {'required': 'Enter Your Phone Number'},
              'email': {'required': 'Enter your Email'}, 
              'course': {'required': 'Enter your Course'},
              'gender': {'required': 'Enter your gender'},
        }  

#User Signup Form
class signUp(UserCreationForm):
    password2=forms.CharField(label='Password(again)',widget=forms.PasswordInput)
    class Meta(UserCreationForm.Meta):
        models=User
        fields=['username','first_name','last_name','email']
        # fields='__all__'
        labels={'email':'Email'} 

# Edit Data for staff
class EditUserData(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','is_active','date_joined','last_login']
        labels={'email':'Email'}


#Edit Data For Admin
class EditAdminData(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields= '__all__'
        labels={'email':'Email'}        