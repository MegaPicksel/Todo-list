from __future__ import absolute_import
from django.core.mail import send_mail
from celery import Celery

# Celery task, sending an email on registration

app = Celery('tasks', broker='amqp://guest:guest@localhost:5672/')

@app.task
def mail(registration_email):
    subject = 'account confirmation'
    message = 'Please click the link to complete registration. http://127.0.0.1:8000/todo/login/'
    from_email = 'django.testacc306@gmail.com'
    to = [registration_email]
    send_mail(subject,
              message,
              from_email,
              to,
              fail_silently=False)












