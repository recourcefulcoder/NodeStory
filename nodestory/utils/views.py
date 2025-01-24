from django.http import HttpResponse


def left_intentionally_blank(request, *args, **kwargs):
    return HttpResponse(
        "<h1>This page was left intentionally blank for now</h1>",
    )
