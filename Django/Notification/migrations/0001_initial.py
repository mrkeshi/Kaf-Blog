from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title',      models.CharField(max_length=200, verbose_name='عنوان')),
                ('message',    models.TextField(verbose_name='متن اعلان')),
                ('type',       models.CharField(choices=[('info','اطلاعات'),('success','موفقیت'),('warning','هشدار'),('error','خطا'),('post','مطلب جدید')], default='info', max_length=20, verbose_name='نوع')),
                ('link',       models.CharField(blank=True, max_length=500, verbose_name='لینک')),
                ('is_active',  models.BooleanField(default=True, verbose_name='فعال')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
            ],
            options={'verbose_name': 'اعلان', 'verbose_name_plural': 'اعلان‌ها', 'ordering': ['-created_at']},
        ),
        migrations.CreateModel(
            name='NotificationRead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_token', models.CharField(db_index=True, max_length=64, verbose_name='توکن مرورگر')),
                ('read_at',      models.DateTimeField(auto_now_add=True, verbose_name='تاریخ خواندن')),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reads', to='Notification.notification', verbose_name='اعلان')),
            ],
            options={'verbose_name': 'خواندن اعلان', 'verbose_name_plural': 'خواندن‌های اعلان', 'unique_together': {('notification', 'client_token')}},
        ),
    ]
