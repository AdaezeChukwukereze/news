# Generated by Django 4.1.5 on 2023-02-07 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_alter_news_options_alter_news_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(default='me'),
        ),
    ]
