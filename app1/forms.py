from django import forms
from .models import House
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
class HouseForm(forms.ModelForm):
    class Meta:
        model=House
        fields='__all__'
        widgets = {
            'purchasing_date': forms.DateInput(attrs={'type': 'date'}),
            'registration_time': forms.TimeInput(attrs={'type': 'time'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']

    def save(self,commit=True):
        ran=super().save(commit=False)
        ran.password=make_password(ran.password)
        ran.save()
        return ran