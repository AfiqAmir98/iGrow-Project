# Generated by Django 4.1.3 on 2022-11-30 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0004_auto_20220609_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
