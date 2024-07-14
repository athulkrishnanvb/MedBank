from django import forms
from .models import Bloodrequest,BloodDonation,MedicalProduct,Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BloodRequestForm(forms.ModelForm):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    bloodgroup = forms.ChoiceField(choices=BLOOD_GROUP_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # master = forms.ModelChoiceField(queryset=Master.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), required=True, label="Category")

    class Meta:
        model = Bloodrequest
        fields = ['patient_name', 'patient_age', 'reason', 'bloodgroup', 'quantity_ml']
        widgets = {
            'patient_name': forms.TextInput(attrs={'class': 'form-control'}),
            'patient_age': forms.NumberInput(attrs={'class': 'form-control'}),
            'reason': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,  # Adjust the number of rows
                'cols': 40   # Adjust the number of columns (optional)
            }),
            'quantity_ml': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class BloodDonationForm(forms.ModelForm):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    blood_group = forms.ChoiceField(choices=BLOOD_GROUP_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # master = forms.ModelChoiceField(queryset=Master.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), required=True, label="Category")

    class Meta:
        model = BloodDonation
        fields = ['donor_name', 'donor_age', 'blood_group', 'quantity_ml']
        widgets = {
            'donor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'donor_age': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity_ml': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required')
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    


class MedicalProductForm(forms.ModelForm):
    class Meta:
        model = MedicalProduct
        fields = ['photo', 'name', 'description', 'quantity', 'available', 'price']
        widgets = {

        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['payment_method','address']
        widgets = {
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
        }
