
from django import forms

class ContactForms(forms.Form):
    name = forms.CharField(label='nombre' , required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'escribe tu nombre'}
    ))
    email = forms.EmailField(label='email', required=True, widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':'escribe tu email'}
    ), min_length=20, max_length=100)
    content = forms.CharField(label='contenido', required=True, widget=forms.Textarea(
         attrs={'class':'form-control', 'rows':3, 'placeholder':'escribe tu mensaje'}
    ))