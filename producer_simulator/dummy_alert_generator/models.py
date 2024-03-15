from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.
class Generic_alert(models.Model):
    class Meta:
        verbose_name = _("Alert")
        verbose_name_plural = _("Alerts")

    name = models.CharField(
        _("name"),
        max_length=100,
    )
    description = models.TextField(
        _("description"),
    )    
    target_team = models.TextField(
        _("target_team"),
    )
    created_at = models.DateTimeField(
        default=timezone.now
    )
   