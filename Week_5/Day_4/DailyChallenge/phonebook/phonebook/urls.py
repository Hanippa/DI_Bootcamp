from django.contrib import admin
from django.urls import path
from phone_app.views import search_person, profile_view , home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("persons/<str:search_value>", search_person),
    path("profiles/<str:search_value>", profile_view),
    path('',home)
]
