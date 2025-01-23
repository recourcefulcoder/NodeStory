from django.urls import path

from utils.views import left_intentionally_blank

from . import views

app_name = "stories"
urlpatterns = [
    path("<int:id>/", views.show_story, name="show_story"),
    path("description/", left_intentionally_blank, name="edit_description"),
    path("content/", left_intentionally_blank, name="create_story"),
]
