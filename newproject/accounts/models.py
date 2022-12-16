from django.db import models

class Account(models.Model):
    class Meta:
        db_table = 'Account'
    email = models.EmailField(max_length=150)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.username