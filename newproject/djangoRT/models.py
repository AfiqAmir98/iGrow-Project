from django.db import models

class DataRT(models.Model):
    class Meta:
        db_table = 'DataRT'
    data = models.IntegerField()

    def __str__(self):
        return self.data
