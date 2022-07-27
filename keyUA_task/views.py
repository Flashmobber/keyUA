from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from keyUA_task.forms import UserCreateForm
from keyUA_task.models import Entry


def index(request):
    all_entrys = Entry.objects.count()

    context = {
        "all_entrys": all_entrys,
    }

    return render(request, "keyUA_task/index.html", context=context)


class UserCreateView(generic.CreateView):
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy("keyUA_task:index")


class EntryListView(LoginRequiredMixin, generic.ListView):
    model = Entry
    fields = ["date", "distance", "duration", ]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class EntryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Entry
    fields = ["id", "date", "distance", "duration", ]
    success_url = reverse_lazy("keyUA_task:entry-list")
