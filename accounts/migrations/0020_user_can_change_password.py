# Generated by Django 4.2.3 on 2023-08-19 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_alter_comment_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='can_change_password',
            field=models.BooleanField(default=False),
        ),
    ]
