# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-10 16:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Clusterizacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecommerce', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('data', models.CharField(max_length=255)),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='cluster.Cluster')),
            ],
        ),
        migrations.AddField(
            model_name='cluster',
            name='clusterizacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clusters', to='cluster.Clusterizacao'),
        ),
    ]
