# Generated by Django 2.2 on 2019-05-22 08:55

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190522_0653'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='initial_state',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, verbose_name='initial state'),
        ),
    ]