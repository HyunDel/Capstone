# Generated by Django 3.0.14 on 2021-05-24 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CapD_rest', '0002_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_key',
        ),
        migrations.AddField(
            model_name='video',
            name='video_file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
