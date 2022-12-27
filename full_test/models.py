from django.db import models
import os
import uuid
from .fields import CustomFileField
from django.contrib.auth.models import User

# Create your models here.


def CustomUploadPath(instance, filename):
    FileExten=filename.split('.')[-1]
    if FileExten.lower() in ['webm', 'mp4', 'flv']:
        filename='{0}.{1}'.format(instance.videoTitle, FileExten)
    return os.path.join('videos', filename)



class VideoUpload(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    videoID=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    videoTitle=models.CharField(max_length=25, null=True, default='Distributor doesn\'t upload title!!')
    uploadTime=models.DateField(auto_now_add=True)

    video=CustomFileField(
        upload_to=CustomUploadPath,
        max_size=600000000,
        content_types=['video/webm','video/mp4'])

    videoIntroduction=models.TextField(blank=True, default='No introduction! Sorry...')

    videoPoster=models.ImageField(
        blank=True, null=True,
        default='videoposters/default videoposter.jpg',
        verbose_name='video_poster',
        upload_to=CustomUploadPath)

    def __str__(self):
        total_size=self.video.size+self.videoPoster.size
        return '{0} : {1}'.format(self.videoTitle, total_size)


    class Meta:
        db_table='VideoUpload_table'
        ordering=['-uploadTime']
        
        

class commentModel(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    video=models.ForeignKey(VideoUpload, on_delete=models.CASCADE)
    user_comment=models.CharField(max_length=300, null=False)
    user_comment_time=models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username}:{self.user_comment_time}"

    class Meta:
        db_table='comment_table'

