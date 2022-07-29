from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import TruncWeek
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from keyUA_task.forms import EntrySearchForm, UserCreateForm
from keyUA_task.models import Entry


def week_number(date1, date2) -> int:
    d1 = date(date1.year, date1.month, date1.day)
    d2 = date(date2.year, date2.month, date2.day)
    return (d2 - d1).days // 7


def index(request):
    queryset = Entry.objects.all()
    if request.user.is_authenticated:
        queryset = Entry.objects.filter(user_id=request.user.id)
    context = {
        "weeks_number": week_number(queryset.first().date,
                                    queryset.last().date),
        "amount_entrys": queryset.count(),
        "total_distance": queryset.aggregate(Sum("distance"))["distance__sum"],
        "total_duration": queryset.aggregate(Sum("duration"))["duration__sum"],
    }
    if request.user.is_authenticated:
        context["week_stat"] = Entry.objects.annotate(
            week=TruncWeek("date")).values("week").annotate(
            dist=Sum("distance")).annotate(
            duration=Sum("duration"))

    return render(request, "keyUA_task/index.html", context=context)


class UserCreateView(generic.CreateView):
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy("keyUA_task:index")


class EntryListView(LoginRequiredMixin, generic.ListView):
    model = Entry
    fields = [
        "date",
        "distance",
        "duration",
    ]
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context["date_filter"] = EntrySearchForm()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_superuser:
            queryset = queryset.filter(user=self.request.user)

        form = EntrySearchForm(self.request.GET)
        date_start = form["date_start"].value()
        date_end = form["date_end"].value()
        if date_start:
            queryset = queryset.filter(date__gte=date_start)
        if date_end:
            queryset = queryset.filter(date__lte=date_end)
        return queryset


class EntryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Entry
    fields = ["id",
              "date",
              "distance",
              "duration",
              ]
    success_url = reverse_lazy("keyUA_task:entry-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EntryUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                      generic.UpdateView):
    model = Entry
    fields = ["id",
              "date",
              "distance",
              "duration",
              ]
    success_url = reverse_lazy("keyUA:entry-list")
    template_name = "keyUA_task/entry_list.html"

    def test_func(self):
        if self.request.user == self.get_object().user:
            return True
        return False


class EntryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Entry
    success_url = reverse_lazy("keyUA:entry-list")
    template_name = "keyUA_task/delete_entry.html"
