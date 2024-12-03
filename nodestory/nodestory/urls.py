from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("homepage.urls", "homepage"), namespace="homepage")),
    path("account/", include(("django.contrib.auth.urls", "auth"),
                             namespace="auth_links")),
    path("story/", include("stories.urls")),
]
