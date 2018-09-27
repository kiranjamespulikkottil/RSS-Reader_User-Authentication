from django import forms

class urlForm(forms.Form):
    urlField = forms.CharField(max_length=100)
