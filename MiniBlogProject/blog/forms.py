from django import forms
from.models import Contact
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from .models import postModel
from django.utils.translation import gettext,gettext_lazy as _
# Form for contact
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        widgets={
            'fullName':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','type':'email','placeholder':'name@gmail.com'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Address'}),
            'subject':forms.TextInput(attrs={'class':'formcontrol','placeholder':'Subject of your message'}),
            'message':forms.Textarea(attrs={'class':'form-control','placeholder':'Write your message here...'})   
        }
        error_messages={
            'fullName': {'required': 'Enter your full name'},
            'email':{'required':'Enter your Email'},
            'address':{'required':'Enter your address'},
            'subject':{'required':'Enter your subject'},
            'message':{'required':'Write some Message'}
        }

#Sign up form
class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Password(Again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta(UserCreationForm.Meta):
        models=User
        fields=['username','first_name','last_name','email']
        labels={
            'username':'Username',
            'first_name':'First Name',
            'last_name':'Last Name',
            'email':"Email"
        }
        
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'})
        }


# Login form 
class LoginForm(AuthenticationForm):
    username=UsernameField (widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'})) 
    password=forms.CharField(label=_("password"),widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))       

# post form
class PostForm(forms.ModelForm):
    class Meta:
        model=postModel
        fields=['title','desc']
        labels={'title':'Title','desc':'Descriptions'}
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Post Title'}),
            'desc':forms.Textarea(attrs={'class':'form-control','placeholder':'Write discription here'}),
            }
        error_messages={
            'title':{'required':'Please Give Titile Of Post'},
            'desc':{'require':'Write your Description'}
            }
    