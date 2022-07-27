from django.contrib import admin

from keyUA_task.models import Entry


class EntryAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if obj.id is None:
            obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Entry, EntryAdmin)
