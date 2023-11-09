from django.db import models

from users.models import CustomUser


class Ad(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='ad title')
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='product price')
    description = models.TextField(verbose_name='product description', blank=True, null=True)
    author = models.ForeignKey(CustomUser, verbose_name='ad author', on_delete=models.CASCADE)
    preview = models.ImageField(verbose_name='ad_preview', upload_to='ads_preview', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creation date')

    class Meta:
        verbose_name = 'Ad'
        verbose_name_plural = 'Ads'

    def __str__(self):
        return self.title
