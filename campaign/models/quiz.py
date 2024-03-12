from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from campaign.models.campaign import Campaign



class Question(models.Model):
    TYPE_CHOICES = (
        ('MCQ', _('Multiple Choice Question')),
        ('TXT', _('Text Response')),
        # Future question types can be added here
    )
    campaign = models.ForeignKey(Campaign, related_name='questions', on_delete=models.CASCADE, verbose_name=_("Campaign"))
    text = models.TextField(verbose_name=_("Question Text"))
    type = models.CharField(max_length=3, choices=TYPE_CHOICES, verbose_name=_("Question Type"))
    correct_text_answer = models.TextField(verbose_name=_("Correct Text Answer"), blank=True, null=True, help_text=_("Applicable for text response type questions"))
    duration = models.PositiveIntegerField(default=10, verbose_name=_("Duration"))  # Added duration field

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE, verbose_name=_("Question"))
    text = models.CharField(max_length=255, verbose_name=_("Choice Text"))
    is_correct = models.BooleanField(default=False, verbose_name=_("Correct Answer"))

    class Meta:
        verbose_name = _("Choice")
        verbose_name_plural = _("Choices")

    def __str__(self):
        return self.text
