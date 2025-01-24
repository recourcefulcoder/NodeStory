from django.db import models
from django.forms import ModelForm

from .models import StoryNode


class BaseNodeCreationForm(ModelForm):
    class Meta:
        model = StoryNode
        fields = ["text"]


class NodeCreationForm(BaseNodeCreationForm):
    title = models.CharField()
