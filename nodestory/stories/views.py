from django.shortcuts import render


def show_story(request, id):
    return render(request, "stories/read_story.html", context={"id": id})


def create_story(request):
    return render(request, "stories/create_story.html")
