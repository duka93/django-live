# Generated by Django 4.1.2 on 2022-10-21 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dijeta_je_meta', '0020_startuserweightandheight_polovi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='startuserweightandheight',
            name='polovi',
        ),
    ]
