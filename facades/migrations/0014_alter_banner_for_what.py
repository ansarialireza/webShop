# Generated by Django 4.2.3 on 2023-09-18 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facades', '0013_alter_banner_for_what'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='for_what',
            field=models.CharField(choices=[('c2', '2col'), ('c3', '3col')], max_length=2),
        ),
    ]
