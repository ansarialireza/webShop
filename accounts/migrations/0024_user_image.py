# Generated by Django 4.2.3 on 2023-09-10 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_watchedproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='web_shop/users/%Y/%m/%d/'),
        ),
    ]
