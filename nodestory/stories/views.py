from http import HTTPStatus

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import UpdateView

from .decorators import user_is_node_owner, user_is_story_owner
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

    def get_success_url(self):
        return reverse(
            "stories:edit_story_node", kwargs={"pk": self.object.pk}
        )

    @method_decorator(login_required)
    @method_decorator(user_is_node_owner)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == HTTPStatus.FOUND:
            messages.success(
                request, _("You have successfully edited story node!")
            )
        return response


class EditStoryDescription(UpdateView):
    model = StoryHead
    form_class = NodeDescriptionForm
    template_name = "stories/edit_story_description.html"
    context_object_name = "head_info"

    def get_success_url(self):
        return reverse(
            "stories:edit_description", kwargs={"pk": self.object.pk}
        )

    @method_decorator(login_required)
    @method_decorator(user_is_story_owner)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
