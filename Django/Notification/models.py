from django.db import models


class Notification(models.Model):
    TYPES = [
        ('info',    'اطلاعات'),
        ('success', 'موفقیت'),
        ('warning', 'هشدار'),
        ('error',   'خطا'),
        ('post',    'مطلب جدید'),
    ]

    title      = models.CharField(max_length=200, verbose_name='عنوان')
    message    = models.TextField(verbose_name='متن اعلان')
    type       = models.CharField(max_length=20, choices=TYPES, default='info', verbose_name='نوع')
    link       = models.CharField(max_length=500, blank=True, verbose_name='لینک')
    is_active  = models.BooleanField(default=True, verbose_name='فعال')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'اعلان'
        verbose_name_plural = 'اعلان‌ها'
        ordering = ['-created_at']

    def __str__(self):
        return f'[{self.get_type_display()}] {self.title}'


class NotificationRead(models.Model):
    notification = models.ForeignKey(
        Notification,
        on_delete=models.CASCADE,
        related_name='reads',
        verbose_name='اعلان'
    )
    client_token = models.CharField(max_length=64, verbose_name='توکن مرورگر', db_index=True)
    read_at      = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ خواندن')

    class Meta:
        verbose_name = 'خواندن اعلان'
        verbose_name_plural = 'خواندن‌های اعلان'
        unique_together = ('notification', 'client_token')

    def __str__(self):
        return f'{self.client_token[:12]}… → #{self.notification_id}'
