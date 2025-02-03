from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import UpdateView

from .forms import NodeCreationForm, NodeDescriptionForm
from .models import StoryHead, StoryNode


def show_story(request, id):
    return render(request, "stories/read_story.html", context={"id": id})


@login_required
def create_story_and_redirect(request):
    new_node = StoryNode.objects.create(author=request.user)
    head = StoryHead.objects.create(first_node=new_node)
    return HttpResponseRedirect(
        reverse("stories:edit_description", args=[head.pk])
    )


class EditStoryNode(UpdateView):
    model = StoryNode
    form_class = NodeCreationForm
    template_name = "stories/edit_story_node.html"
    context_object_name = "story_node"


class EditStoryDescription(UpdateView):
    model = StoryHead
    form_class = NodeDescriptionForm
    template_name = "stories/edit_story_description.html"
    context_object_name = "head_info"
