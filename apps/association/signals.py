import os

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post, Device



@receiver(post_save, sender=Post)
def send_message(sender, instance, created, **kwargs):
    if created:
        print("... enviando notificaciones ...")

        key = 'AAAAwBs19Fo:APA91bFox2kJibOaGhH5sll4fUbjQb9RWXa2SLmMV0j25QDt3z-BRQizjg1IFGNUN3TeAA2G9SbduoPD5F0K4RF1DRuvaJJp9VLuZP5kKqMb5DBxsd_7HSfplVm4t-Dws0aw_Td1CFcZ'

        title = "nueva entrada"
        body = instance.title
        icon = "/assets/img/icono160x160.png"

        devices = Device.objects.filter(active=True)

        for device in devices:
            token = device.token 
            command = "curl https://fcm.googleapis.com/fcm/send --header \"Authorization:key=%s\" --header \"Content-Type:application/json\" -d '{ \"notification\": { \"title\": \"%s\", \"body\": \"%s\", \"icon\": \"%s\" }, \"to\" : \"%s\" }'" % (key, title, body, icon, token)
            os.system(command)
