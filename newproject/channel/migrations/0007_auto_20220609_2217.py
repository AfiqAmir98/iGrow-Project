# Generated by Django 3.1.7 on 2022-06-09 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0006_auto_20220609_1631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='channel_name',
            new_name='channelname',
        ),
    ]
