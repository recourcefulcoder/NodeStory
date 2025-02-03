from ckeditor.fields import RichTextField

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class Tag(models.Model):
    name = models.CharField(max_length=50)


class ClosureTable(models.Model):
    ancestor = models.ForeignKey(
        "StoryNode",
        on_delete=models.CASCADE,
        related_name="children",
        null=True,
    )
    descendant = models.ForeignKey(
        "StoryNode",
        on_delete=models.CASCADE,
        related_name="parents",
        null=True,
    )
    depth = models.SmallIntegerField()


class StoryManager(models.Manager):
    def create(self, ancestor=None, **kwargs):
        created_object = super(StoryManager, self).create(**kwargs)
        if ancestor:
            records = ClosureTable.objects.filter(descendant=ancestor)
            for record in records:
                if record.descendant != record.ancestor:
                    ClosureTable.objects.create(
                        ancestor=record.ancestor,
                        descendant=created_object,
                        depth=1 + record.depth,
                    )
            ClosureTable.objects.create(
                ancestor=ancestor,
                descendant=created_object,
                depth=1,
            )
        else:
            ClosureTable.objects.create(
                ancestor=created_object,
                descendant=created_object,
                depth=0,
            )
        return created_object


class StoryNode(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        null=True,
        on_delete=models.SET_NULL,
    )
    # NULL will mean that post's author account is deleted

    text = RichTextField()
    tags = models.ManyToManyField(Tag)
    published = models.BooleanField(default=False)
    objects = StoryManager()

    def get_absolute_url(self):
        return reverse("stories:show_story", args={self.pk})


class StoryHead(models.Model):
    title = models.CharField(max_length=250, default=_("No title"))
    first_node = models.OneToOneField(
        StoryNode,
        on_delete=models.DO_NOTHING,
        # I should write referencing to the next story node
        # or restrict from deletion first node at all
        related_name="head_info",
    )
    tags = models.ManyToManyField(Tag)
