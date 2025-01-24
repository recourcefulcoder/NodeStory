from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import UpdateView

from .forms import NodeCreationForm
from .models import StoryHead, StoryNode


def show_story(request, id):
    return render(request, "stories/read_story.html", context={"id": id})


@login_required
def create_story_and_redirect(request):
    new_node = StoryNode.objects.create(author=request.user)
    StoryHead.objects.create(first_node=new_node)
    return HttpResponseRedirect(
        reverse("stories:edit_story_node", args=[new_node.pk])
    )


class EditStoryNode(UpdateView):
    model = StoryNode
    form_class = NodeCreationForm
    template_name = "stories/edit_story_node.html"


class EditStoryDescription(UpdateView):
    model = StoryNode
    form_class = NodeCreationForm
    template_name = "stories/edit_story_description.html"
