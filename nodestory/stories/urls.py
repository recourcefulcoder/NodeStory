from django.urls import path

from . import views

app_name = "stories"
urlpatterns = [
    path("<int:id>/", views.show_story, name="show_story"),
    path("create/", views.create_story, name="create_story"),
]
