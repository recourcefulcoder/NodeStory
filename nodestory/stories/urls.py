from django.urls import include, path

from . import views

edit_block = [
    path(
        "description/<int:pk>/",
        views.EditStoryDescription.as_view(),
        name="edit_description",
    ),
    path(
        "contents/<int:pk>/",
        views.EditStoryNode.as_view(),
        name="edit_story_node",
    ),
]
# do NOT change keyword name "PK", as it is used in templates for
# communication between different parts of story editing pages

app_name = "stories"
urlpatterns = [
    path("<int:id>/", views.show_story, name="show_story"),
    path("create_new/", views.create_story_and_redirect, name="create_story"),
    path("edit/", include(edit_block)),
]
