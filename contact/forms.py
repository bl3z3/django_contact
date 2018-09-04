from django import forms

class ContactForm(forms.Form):
	contact_name = forms.CharField()
	contact_email = forms.EmailField()
	content = forms.CharField(widget=forms.Textarea)