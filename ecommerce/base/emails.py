from django.core.mail import send_mail
from django.conf import settings
import uuid



def send_account_activation_email(email,email_token=None):
    subject = 'Activate your account'
    message = f'Please use the following link to activate your account http://127.0.0.1:8000/accounts/activate/{email_token}'
    email_from = settings.EMAIL_HOST_USER
    if not email_token:
        email_token = str(uuid.uuid4())
        subject = subject
        email_from = email_from
        message = message
       


    send_mail(subject, message,email_from, [email])
    