# Generated by Django 4.1.2 on 2022-10-20 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dijeta_je_meta', '0007_newweight'),
    ]

    operations = [
        migrations.AddField(
            model_name='newweight',
            name='nova_tezina',
            field=models.IntegerField(default=0),
        ),
    ]