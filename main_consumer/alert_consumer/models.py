from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class GenericAlert(models.Model):
    name = models.CharField(
        _("name"),
        max_length=100
    )
    description = models.TextField(
        _("description")
    )
    target_team = models.CharField(
        _("target_team"),
        max_length = 100
    )
    # we need also to add the updated_at 
    created_at = models.DateTimeField(
        _("created_at"),
    )

