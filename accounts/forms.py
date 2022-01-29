from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

HOSTELS=[
        ('Brahmaputra', 'Brahmaputra'),
        ('Dihing', 'Dihing'),
        ('Manas', 'Manas'),
        ('Lohit', 'Lohit'),
        ('Dhansiri', 'Dhansiri'),
        ('Kapili', 'Kapili'),
        ('Siang', 'Siang'),
        ('Kameng', 'Kameng'),
        ('Umiam', 'Umiam'),
        ('Barak', 'Barak'),
        ('Subhansiri', 'Subhansiri'),
        ('Disang/Dibang', 'Disang/Dibang'),
]


def emailcheck(value):
    if(value[-11::]!='@iitg.ac.in'):
        raise forms.ValidationError("You must use email-id provided by IIT-Guwahati.")

class UserForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}), validators=[emailcheck])
    class Meta():
        model=User
        fields=('username','email','password')

# def clean_email(self):
#     email=self.cleaned_data['email']
#     if(email(11,))

class UserProfileForm(forms.ModelForm):

    hostel=forms.ChoiceField(required=True, choices=HOSTELS)

    class Meta():
        model=UserProfile
        fields=('hostel', 'profile_pic')
