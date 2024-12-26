from django.db import models

class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em',
        auto_now_add=True,
        auto_now_add=False
    )
    modified = models.DateTimeField(
        'modificado em',
        auto_now_add=false,
        auto_now=True
    )

    class Meta:
        abstract = True
