from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Campaign(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    start_date = models.DateTimeField(verbose_name=_("Start Date"))
    end_date = models.DateTimeField(verbose_name=_("End Date"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    prize_description = models.TextField(verbose_name=_("Prize Description"), blank=True, null=True)
    winner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='campaign_winner', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Winner"))
    runner_up = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='campaign_runner_up', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Runner Up"))
    third_place = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='campaign_third_place', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Third Place"))

    class Meta:
        verbose_name = _("Campaign")
        verbose_name_plural = _("Campaigns")

    def __str__(self):
        return self.title

    @property
    def is_current(self):
        """Check if the campaign is currently active based on the start and end dates."""
        from django.utils.timezone import now
        return self.start_date <= now() <= self.end_date
