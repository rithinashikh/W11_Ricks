# Generated by Django 4.1.4 on 2023-02-28 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phase', '0002_banner_alter_order_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='is_expired',
            new_name='is_active',
        ),
    ]
