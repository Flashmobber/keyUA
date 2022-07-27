from django.urls import path

from .views import index, EntryListView, EntryCreateView, UserCreateView

urlpatterns = [
    path("", index, name="index"),
    path("entry/", EntryListView.as_view(), name="entry-list"),
    path("entry/add", EntryCreateView.as_view(), name="entry-add"),
    path("users/create/", UserCreateView.as_view(), name="user-create"),
]

app_name = "keyUA_task"
