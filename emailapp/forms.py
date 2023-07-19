from django import forms

class EmailForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    recipients = forms.CharField(label='To', widget=forms.Textarea)
    message = forms.CharField(widget=forms.Textarea)