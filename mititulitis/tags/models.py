from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name of the learning path")
    is_certificate = models.BooleanField(verbose_name="This learning path involves a certificate or exam",
                                         default=False, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")

    def __str__(self):
        return self.name
