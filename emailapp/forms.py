from django import forms

class EmailForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    recipient = forms.EmailField(label='To')
    message = forms.CharField(widget=forms.Textarea)