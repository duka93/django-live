# Generated by Django 4.1.2 on 2022-10-26 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dijeta_je_meta', '0025_alter_currentweight_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='startuserweightandheight',
            name='stepen_gubitka_tezine',
        ),
    ]
