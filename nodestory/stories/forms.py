from ckeditor.widgets import CKEditorWidget

from django import forms

from .models import StoryHead, StoryNode


class NodeCreationForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = StoryNode
        exclude = ["date_created", "author"]


class NodeDescriptionForm(forms.ModelForm):
    class Meta:
        model = StoryHead
        fields = ["title", "tags"]
