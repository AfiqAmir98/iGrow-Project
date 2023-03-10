# Generated by Django 3.2.7 on 2022-01-09 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150)),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'Account',
            },
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
