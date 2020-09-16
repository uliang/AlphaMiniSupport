from django.db import models

# Create your models here.


class Message(models.Model) :
    message = models.CharField(max_length=1000, verbose_name='Message')
    created_on = models.DateTimeField(verbose_name="Date created", auto_now_add=True)
    updated_on = models.DateTimeField(verbose_name="Date last updated", auto_now=True)
    message_start = models.TimeField(verbose_name="Repeat message start time") 
    message_end = models.TimeField(verbose_name="Repeat message stop time", null=True, blank=True)
    message_duration = models.DurationField(verbose_name="Repeat message duration", null=True, blank=True)
    frequency = models.DurationField(verbose_name="Repeat message every")
    active = models.BooleanField(verbose_name="Active message", default=True)

    def __str__(self) : 
        display_message = ' '.join(self.message.split()[:10]) + '...'
        return f"<{display_message}, in_use={self.active}>"