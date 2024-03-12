from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from campaign.models.campaign import Campaign


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=30)
    address = models.TextField()
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    @property
    def total_campaigns_played(self):
        """Returns the total number of campaigns the player has participated in."""
        # Assuming there's a UserAnswer or similar model that records every answer submission
        # This requires a model that associates users with campaigns they've participated in
        # For simplicity, this is a placeholder implementation
        return Campaign.objects.filter(questions__useranswer__user=self.user).distinct().count()

    @property
    def total_wins(self):
        """Returns the total number of wins (1st, 2nd, and 3rd places)."""
        winner_count = Campaign.objects.filter(winner=self.user).count()
        runner_up_count = Campaign.objects.filter(runner_up=self.user).count()
        third_place_count = Campaign.objects.filter(third_place=self.user).count()
        return winner_count + runner_up_count + third_place_count

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)
