# Generated by Django 2.0.5 on 2018-07-01 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.TextField(default=None),
        ),
    ]