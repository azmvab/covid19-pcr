from uuid import uuid4
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .mixins import TimeStampModel


class Person(TimeStampModel):
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
    birthday = models.DateField(verbose_name=_("Birthday"))
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
    result_time = models.DateTimeField()
    result = models.CharField(
        choices=(
            ("Negative", "Negative"),
            ("Positive", "Positive"),
        ),
        max_length=32
    )


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("People")
