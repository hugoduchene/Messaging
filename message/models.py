from django.db import models
from django.utils import timezone
from user.models import CustomUser

# Create your models here.


class Message(models.Model):
    date_message = models.DateField(default=timezone.now)
    content_message = models.TextField(
        default="he wanted to make a joke and he didn't write anything down. you're huge man !"
    )
    id_giving = models.ForeignKey(CustomUser, related_name='message_giving', on_delete=models.CASCADE)
    id_receiving = models.ForeignKey(CustomUser, related_name='message_receiving', on_delete=models.CASCADE)
