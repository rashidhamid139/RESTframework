import string
import glob 
import os, io
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, send_mail, mail_admins
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.conf import settings

@shared_task
def create_random_user_accounts(total):
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password)
    return '{} random users created with success!'.format(total)


@shared_task(name='print_msg_with_me')
def print_msg(name, *args, **kwargs):
    print("Celery is working!! {} has implemented it correctly".format(name))


@shared_task(name='add_function')
def add(x, y):
    print("Add function has been called with params!{} {}".format(x,y))
    return x+y

@shared_task
def send_activation_mail(user_id, context):
    user = User.objects.get(id=user_id)

    context.update({
        'username': user.username,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),

    })

    send_mail('subject', 'rashidhamid139@gmail.com', settings.DEFAULT_FROM_EMAIL, [user.email])
