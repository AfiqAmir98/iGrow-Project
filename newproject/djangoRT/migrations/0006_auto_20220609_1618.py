# Generated by Django 3.1.7 on 2022-06-09 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoRT', '0005_auto_20220609_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datart',
            name='data',
            field=models.IntegerField(),
        ),
    ]
