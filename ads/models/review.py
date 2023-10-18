from django.db import models

from ads.models.ad import Ad
from users.models import CustomUser


class Review(models.Model):
    text = models.TextField(verbose_name='contents')
    author = models.ForeignKey(CustomUser, verbose_name='author', on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, verbose_name='reviewed ad', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creation date')

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f'{self.pk} review'
