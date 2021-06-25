from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)
    is_certificate = models.BooleanField(verbose_name="This learning path involves a certificate or exam", default=False, blank=True)
