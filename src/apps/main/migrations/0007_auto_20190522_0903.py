# Generated by Django 2.2 on 2019-05-22 09:03

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_game_initial_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='initial_state',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, verbose_name='initial state (rules)'),
        ),
    ]
