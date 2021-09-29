from django.db import models


class Worker(models.Model):
    fio = models.CharField(
        verbose_name='Name',
        max_length=50,
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = 'worker'
        verbose_name_plural = 'workers'

    def __str__(self):
        return self.fio
