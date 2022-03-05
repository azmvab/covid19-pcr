from uuid import uuid4

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from .mixins import TimeStampModel


class Person(TimeStampModel):
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="people_added_by",
        verbose_name=_("Added by"),
    )
    guid = models.UUIDField(
        verbose_name=_("UUID"),
        default=uuid4,
        editable=False,
        unique=True
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=128,
    )
    birthday = models.DateField(verbose_name=_("Birthday"), blank=True, null=True)
    mobile = models.CharField(
        verbose_name=_("Mobile"),
        max_length=16,
    )
    nationality = models.CharField(max_length=128)
    identification_type = models.CharField(
        choices=(
            ("Passport", "Passport"),
            ("ID", "ID"),
        ),
        max_length=128
    )
    identification_id = models.CharField(
        verbose_name=_("Identification ID"),
        max_length=128,
    )
    gender = models.CharField(
        choices=(
            ("Male", "Male"),
            ("Female", "Female"),
        ),
        max_length=32
    )
    collection_time = models.DateTimeField(null=True)
    result_time = models.DateTimeField()
    result = models.CharField(
        choices=(
            ("Negative", "Negative"),
            ("Positive", "Positive"),
        ),
        max_length=32
    )
    report_no = models.CharField(max_length=128, blank=True, default="")
    hesn_no = models.CharField(max_length=128, blank=True, default="")

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("People")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("people:people-detail", kwargs={"slug": self.guid})
