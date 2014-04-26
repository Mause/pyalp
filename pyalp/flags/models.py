from django.db import models


class Flag(models.Model):
    name = models.CharField(
        max_length=20, help_text="The name of the flag")
    description = models.TextField(
        "A brief description of the flag", default='')
    enabled = models.BooleanField("Whether or not the flag is enabled")

    def __str__(self):
        return '{} : {}'.format(
            self.name,
            'enabled' if self.enabled else 'disabled'
        )
