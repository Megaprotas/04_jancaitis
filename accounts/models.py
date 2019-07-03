from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfileManager(models.Manager):
    pass


class Profile(models.Model):
    NOOB = 'noob'
    STUDENT = 'student'
    MID = 'mid'
    PRO = 'pro'
    STATUS = (
        (NOOB, 'noob'),
        (STUDENT, 'student'),
        (MID, 'mid'),
        (PRO, 'pro')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=100, default='')
    status = models.CharField(max_length=20, choices=STATUS, default=STUDENT)
    website = models.URLField(default='')
    image = models.ImageField(default='images/profile.jpg', upload_to='images')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


