from ckeditor.widgets import CKEditorWidget

from django import forms
from django.utils.translation import gettext as _

from .models import StoryHead, StoryNode


class NodeCreationForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(), label=_("Text"))

    class Meta:
        model = StoryNode
        exclude = ["date_created", "author"]
        labels = {
            "text": _("text"),
            "published": _("publish node"),
            "tags": _("tags"),
        }


class NodeDescriptionForm(forms.ModelForm):
    class Meta:
        model = StoryHead
        fields = ["title", "tags"]
        labels = {
            "title": _("title"),
            "tags": _("tags"),
        }
