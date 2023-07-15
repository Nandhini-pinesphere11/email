from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import EmailForm


def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            recipient = form.cleaned_data['recipient']
            message = form.cleaned_data['message']
            
            send_mail(
                'Subject',
                message,
                name + ' <sender@example.com>',  # Replace 'sender@example.com' with your actual email address
                [recipient],
                fail_silently=False,
            )
            
            return redirect('email_success')
    else:
        form = EmailForm()
    
    return render(request, 'email_form.html', {'form': form})

def email_success(request):
    return render(request, 'email_success.html')