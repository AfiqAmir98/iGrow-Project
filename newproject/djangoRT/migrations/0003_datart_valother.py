# Generated by Django 4.0.4 on 2022-05-17 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoRT', '0002_rename_rtdata_datart_alter_datart_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='datart',
            name='valOther',
            field=models.IntegerField(default=150, max_length=150),
            preserve_default=False,
        ),
    ]
