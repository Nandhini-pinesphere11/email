from django import forms

class EmailForm(forms.Form):
    sender = forms.EmailField(label='From')
    recipient = forms.EmailField(label='To')
    message = forms.CharField(widget=forms.Textarea)
