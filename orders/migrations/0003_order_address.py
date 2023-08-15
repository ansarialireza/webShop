# Generated by Django 4.2.3 on 2023-08-15 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_alter_comment_rating'),
        ('orders', '0002_order_deliveried_order_packing_order_processed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.address'),
            preserve_default=False,
        ),
    ]
