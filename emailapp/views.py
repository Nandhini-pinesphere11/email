from django.shortcuts import render, redirect
from .forms import EmailForm
from django.core.mail import send_mail

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            recipients = [email.strip() for email in form.cleaned_data['recipients'].split(',')]
            message = form.cleaned_data['message']

            send_mail(
                'Subject',
                message,
                'sender@example.com',
                recipients,
                fail_silently=False,
            )

            return redirect('email_success')
    else:
        form = EmailForm()

    return render(request, 'email_form.html', {'form': form})


def email_success(request):
    return render(request, 'email_success.html')