from django.db import models

# Create your models here.

class Chart(models.Model):
    class Meta:
        db_table = 'charts'
    name_y = models.CharField(max_length=100, null=False, blank=False)
    num_x = models.IntegerField()

    def __str__(self):
        return f'{self.name_y} - {self.num_x}'
