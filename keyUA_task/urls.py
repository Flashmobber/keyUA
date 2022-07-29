from django.urls import path

from .views import index, EntryListView, EntryCreateView, UserCreateView, \
    EntryUpdateView, EntryDeleteView

urlpatterns = [
    path("", index, name="index"),
    path("entry/", EntryListView.as_view(), name="entry-list"),
    path("entry/add/", EntryCreateView.as_view(), name="entry-add"),
    path("entry/<int:pk>/update/", EntryUpdateView.as_view(),
         name="entry-update"),
    path("entry/<int:pk>/delete/", EntryDeleteView.as_view(), name="entry-delete"),
    path("accounts/create/", UserCreateView.as_view(), name="user-create"),
]

app_name = "keyUA_task"
