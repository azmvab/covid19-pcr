from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', "birthday", "get_absolute_url", "get_absolute_img_url")
    list_display_links = ('name', 'birthday')
    search_fields = ('name', 'identification_id')
    list_filter = ('created', )
    readonly_fields = ("added_by", "guid", "get_absolute_url", "get_absolute_img_url")

    def get_absolute_url(self, obj):
        return format_html('<a href="{}">Detail</a>', obj.get_absolute_url())

    def get_absolute_img_url(self, obj):
        url = reverse("people:people-detail-img", kwargs={"slug": obj.guid})
        return format_html('<a href="{}">Image</a>', url)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(added_by=request.user)
        return queryset

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        obj.save()

    def has_view_or_change_permission(self, request, obj=None):
        ret = super().has_view_or_change_permission(request, obj)

        if obj is not None:
            return ret and obj.added_by == request.user
        return ret


admin.site.register(Person, PersonAdmin)
