# Generated by Django 4.0.1 on 2022-02-11 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('full_test', '0004_alter_videoupload_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videoupload',
            options={'ordering': ['-uploadTime']},
        ),
        migrations.AlterModelTable(
            name='videoupload',
            table='VideoUpload_table',
        ),
    ]
