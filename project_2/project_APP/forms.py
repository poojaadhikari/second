from django import forms
from django.forms import widgets
from datetime import datetime


class employeeForm(forms.Form):
    FAVOURITE_COLOR_CHOICES = [
        ('green', 'green'),
        ('yellow', 'yellow'),
        ('orange', 'orange'),
        ('purple', 'purple'),
        ('blue', 'blue'),
    ]
    name = forms.CharField(initial="Enter your name")
    favourite_color = forms.ChoiceField(choices=FAVOURITE_COLOR_CHOICES)
    email = forms.EmailField(initial="Enter your email")
    password = forms.CharField(initial="Enter your password")
    employee_data = forms.CharField(widget=forms.Textarea)
    headline = forms.CharField(widget=forms.Textarea(attrs={"rows":2}))
    day = forms.DateField(initial=datetime.now())
