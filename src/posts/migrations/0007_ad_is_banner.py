# Generated by Django 4.2.4 on 2023-11-04 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_ad_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='is_banner',
            field=models.BooleanField(default=True),
        ),
    ]