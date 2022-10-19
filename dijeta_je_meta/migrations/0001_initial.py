# Generated by Django 4.1.2 on 2022-10-19 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StarUserWeightAndHeight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_weight', models.IntegerField(max_length=3)),
                ('height', models.IntegerField(max_length=3)),
                ('diet_pace', models.CharField(choices=[('Moderate pace', 'Moderate pace'), ('Aggressive pace', 'Aggressive pace')], default='Moderate pace', max_length=20)),
            ],
        ),
    ]
