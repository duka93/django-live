# Generated by Django 4.1.2 on 2022-10-21 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dijeta_je_meta', '0018_alter_test_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='startuserweightandheight',
            old_name='trenutna_tezina',
            new_name='pocetna_tezina',
        ),
    ]