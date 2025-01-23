from django.shortcuts import render
from django.views.generic import FormView

from .forms import StoryCreationForm


def show_story(request, id):
    return render(request, "stories/read_story.html", context={"id": id})


class CreateStory(FormView):
    form_class = StoryCreationForm
    template_name = "stories/create_story.html"
