from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimeStampModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created")
    )

    modified = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Last modified")
    )

    def __str__(self):
        format = "%B %d, %Y, %I:%M %p"
        return _("Created: %s, Last modified: %s" % (self.created.strftime(format), self.modified.strftime(format)))

    class Meta:
        abstract = True
        verbose_name = _("TimeStamp")
        verbose_name_plural = _("TimeStamps")
