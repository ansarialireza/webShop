# Generated by Django 4.2.3 on 2023-09-18 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_articlecomment_and_more'),
        ('blog', '0007_article_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecomment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.article'),
        ),
    ]
