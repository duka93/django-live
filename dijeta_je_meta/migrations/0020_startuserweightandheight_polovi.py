# Generated by Django 4.1.2 on 2022-10-21 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dijeta_je_meta', '0019_rename_trenutna_tezina_startuserweightandheight_pocetna_tezina'),
    ]

    operations = [
        migrations.AddField(
            model_name='startuserweightandheight',
            name='polovi',
            field=models.CharField(choices=[('Muški', 'Muški'), ('Ženski', 'Ženski')], default=1, max_length=6),
            preserve_default=False,
        ),
    ]
