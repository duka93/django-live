# Generated by Django 4.1.2 on 2022-10-20 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dijeta_je_meta', '0013_newweight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newweight',
            name='current_user',
        ),
    ]