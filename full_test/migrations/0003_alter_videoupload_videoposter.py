# Generated by Django 4.0.1 on 2022-02-11 09:45

from django.db import migrations, models
import full_test.models


class Migration(migrations.Migration):

    dependencies = [
        ('full_test', '0002_videoupload_videoposter_alter_videoupload_video_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoupload',
            name='videoPoster',
            field=models.ImageField(blank=True, default='videoposters/default videoposter.jpg', null=True, upload_to=full_test.models.CustomUploadPath, verbose_name='avartars'),
        ),
    ]