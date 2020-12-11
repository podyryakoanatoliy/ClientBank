from django import forms
from django.forms import SelectDateWidget


class UserForm(forms.Form):
    YEARS = [x for x in range(1940, 2020)]
    name = forms.CharField()
    surname = forms.CharField()
    birthday = forms.DateField(widget=SelectDateWidget(years=YEARS))
    card = forms.RegexField(min_length=16, max_length=16, help_text="XXXX-XXXX-XXXX-XXXX")
    phone = forms.RegexField(r"^\+?3?8?(0[5-9][0-9]\d{7})$", help_text="+38-0XX-XXX-XXXX", max_length=13, min_length=10)
    email = forms.EmailField()



