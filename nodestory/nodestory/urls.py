from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("homepage.urls", namespace="homepage")),
    path("account/", include("django.contrib.auth.urls")),
    path("account/", include("users.urls", namespace="account")),
    path("story/", include("stories.urls", namespace="stories")),
]
