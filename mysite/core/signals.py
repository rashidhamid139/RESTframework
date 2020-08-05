from django.db.models.signals import post_save
from dajngo.dispatch import reciever
from .models import InputImage, OutputImage
from .tasks import save_image_to_models


@reciever(post_save, sender=InputImage)
def save_image_to_model(sender, **kwargs):
    save_image_to_models.delay()