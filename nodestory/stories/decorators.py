from functools import wraps

from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.utils.translation import gettext as _

from .models import StoryHead, StoryNode


def user_is_object_owner(wrapped, model):
    def decorate_function(f):
        @wraps(f)
        def decorated_function(request, *args, **kwargs):
            pk = kwargs.get("pk")
            try:
                obj_author = model.objects.get(pk=pk).author
            except model.DoesNotExist:
                return render(
                    request,
                    "message.html",
                    context={
                        "message": _("Object with provided id does not exist")
                    },
                )

            if not request.user.is_superuser and obj_author != request.user:
                raise PermissionDenied
            return f(request, *args, **kwargs)

        return decorated_function

    return decorate_function(wrapped)


def user_is_node_owner(wrapped):
    return user_is_object_owner(wrapped, StoryNode)


def user_is_story_owner(wrapped):
    return user_is_object_owner(wrapped, StoryHead)
