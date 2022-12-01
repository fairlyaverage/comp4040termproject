from django.db import models
from django.forms import DateTimeField
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Moment(models.Model):
    moment_text = models.TextField(help_text='Text body for a Moment')
    moment_created = models.DateTimeField(help_text='Moment created at')
    moment_edited = models.DateTimeField(help_text='Moment last edited at', blank=True, null=True)

    # to-do: needs Fk field to User
    moment_by = models.ForeignKey('Momenteer', on_delete=models.SET_NULL, null=True)

    # Metadata
    class Meta:
        ordering = ['moment_created'] # index Moments from most to least recent

    def get_absolute_url(self):
        """ Returns a URL for a particular Moment """
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """ String to describe a particular Moment. """
        # To-Do
        return str(self.moment_created)

# class Momenteer(AbstractUser):
class Momenteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Momenteer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

    """
        USERNAME_FIELD
        EMAIL_FIELD
    """



    # def __str__(self):
    #     return self.username
    # pass
