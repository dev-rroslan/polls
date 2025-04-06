from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    contact = forms.CharField(max_length=100, required=True, label="Phone or Email")
    message = forms.CharField(widget=forms.Textarea, required=True)
