from email.policy import default
from .fields import CustomImageField
from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.



def CustomFilePath(instance, filename):
    file_exten=filename.split('.')[-1]
    filename=f'{instance.connected.username}_avatar.{file_exten}'
    return os.path.join('avatars',instance.connected.username, filename)

def AutoAlternate():
    
    pass

class Profiles(models.Model):
    connected=models.OneToOneField(User,
                                    on_delete=models.CASCADE)
    created_time=models.DateField(auto_now_add=True)
    user_avatar=CustomImageField(upload_to=CustomFilePath,
                                  default='default_avatar.png',
                                  content_types=['image/jpeg','image/png', 'image/jpg'],
                                  max_size=10240000)

    user_signature=models.CharField(max_length=50, default='This man is too lazy to write anything.')

    def __str__(self):
        return f'{self.connected.username},created since {self.created_time}'

    class Meta:
        db_table='user_profile_table'
        verbose_name='user_profile'