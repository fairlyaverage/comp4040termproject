from django.db import models
from django.forms import DateTimeField
from django.urls import reverse

class Moment(models.Model):
    moment_text = models.TextField(help_text='Text body for a Moment')
    moment_created = models.DateTimeField(help_text='Moment created at')
    moment_edited = models.DateTimeField(help_text='Moment last edited at')

    # to-do: needs Fk field to User

    # Metadata
    class Meta:
        ordering = ['moment_created'] # index Moments from most to least recent

    def get_absolute_url(self):
        """ Returns a URL for a particular Moment """
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """ String to describe a particular Moment. """
        # To-Do
        return self
