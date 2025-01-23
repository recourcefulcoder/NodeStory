from django.db import models
from django.forms import ModelForm

from .models import StoryNode


class NodeCreationForm(ModelForm):
    class Meta:
        model = StoryNode
        fields = ["text"]


class StoryCreationForm(NodeCreationForm):
    title = models.CharField()
