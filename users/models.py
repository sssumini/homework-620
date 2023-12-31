from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# 리시버 Import

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followings = models.ManyToManyField("self", related_name="followers", symmetrical=False)

# 팔로잉 리시버

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwnargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()