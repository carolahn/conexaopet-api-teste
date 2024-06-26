from django.db import models
from pet.models import Pet
from django.conf import settings
import os

class Event(models.Model):
    pets = models.ManyToManyField(Pet, related_name='events', blank=True)
    pets_ids = models.CharField(max_length=255, default='', blank=True)
    date_hour_initial = models.DateTimeField()
    date_hour_end = models.DateTimeField()
    address = models.ForeignKey('address.Address', on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    is_confirmed = models.BooleanField(default=False)
    followers = models.IntegerField(default=0)

    class Meta:
        db_table = 'event'


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='event_images/')
    order_number = models.IntegerField(default=0)
    custom_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'event_image'

    def delete(self, *args, **kwargs):
        if self.image:
            try:
                os.remove(self.image.path)
            except FileNotFoundError:
                pass 

        super(EventImage, self).delete(*args, **kwargs)