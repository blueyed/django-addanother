# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-08 16:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='current_team',
            field=models.ForeignKey(help_text='This demonstrate the wrapper adding a create button only', on_delete=django.db.models.deletion.CASCADE, related_name='current_players', to='testapp.Team'),
        ),
        migrations.AddField(
            model_name='player',
            name='future_team',
            field=models.ForeignKey(help_text='This demonstrate the wrapper adding both a create and an edit button', on_delete=django.db.models.deletion.CASCADE, related_name='future_players', to='testapp.Team'),
        ),
        migrations.AddField(
            model_name='player',
            name='previous_teams',
            field=models.ManyToManyField(help_text='This demonstrate the wrapper on a ManyToMany field', related_name='ancient_players', to='testapp.Team'),
        ),
    ]
