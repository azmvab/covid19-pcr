from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('guid', 'name', "get_absolute_url", "get_absolute_img_url")
    list_display_links = ('guid', 'name', )
    search_fields = ('name', )

    def get_absolute_url(self, obj):
        return format_html('<a href="{}">Detail</a>', obj.get_absolute_url())

    def get_absolute_img_url(self, obj):
        url = reverse("people:people-detail-img", kwargs={"slug": obj.guid})
        return format_html('<a href="{}">Image</a>', url)

admin.site.register(Person, PersonAdmin)
