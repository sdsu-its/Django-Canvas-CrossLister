from django import forms


class inputForm(forms.Form):
    api = forms.CharField(max_length=100)
    shell = forms.CharField(max_length=100)

