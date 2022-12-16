from django.forms import ModelForm
from . models import Channel, Comment

class CreateChannel(ModelForm):
    class Meta:
        model = Channel
        fields = ['name', 'slug', 'description', 'metadata', 'location', 'soil']

class CreateComment(ModelForm):
	class Meta:
		model = Comment
		fields = ['name', 'body']