from datetime import date
from django.db import models

# Create your models here.


class Message(models.Model) :
    message = models.CharField(max_length=1000, verbose_name='Message')
    created_on = models.DateTimeField(verbose_name="Date created", auto_now_add=True)
    updated_on = models.DateTimeField(verbose_name="Date last updated", auto_now=True)
    message_start_date = models.DateField(verbose_name="Day to start playing message", default=date.today) 
    message_end_date = models.DateField(verbose_name="Day to end playing message", default=date.today)
    message_start = models.TimeField(verbose_name="Repeat message start time") 
    message_end = models.TimeField(verbose_name="Repeat message stop time", null=True, blank=True)
    frequency = models.DurationField(verbose_name="Repeat message every (hh:mm:ss)")

    def __str__(self) : 
        display_message = ' '.join(self.message.split()[:10]) + '...'
        return f"<{display_message}>"