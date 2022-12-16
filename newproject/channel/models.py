from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Channel(models.Model):
    class Meta:
        db_table = 'channel'
    name = models.CharField(max_length=120)
    slug = models.SlugField()
    description = models.TextField()
    metadata = models.FileField(blank=True)
    location = models.CharField(max_length=120)
    date = models.DateField(auto_now_add=True)
    soil = models.CharField(max_length=120)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def snippet(self):
        return self.description[:50] + '...'

class Comment(models.Model):
    class Meta:
        db_table = 'comment'
    channelname = models.ForeignKey(Channel, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.channelname.name, self.name)
