# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Clusterizacao (models.Model):
    ecommerce = models.CharField(max_length=255)

class Cluster (models.Model):
    clusterizacao = models.ForeignKey(Clusterizacao,related_name='clusters')
    title = models.CharField(max_length=255)

class Review (models.Model):
    cluster = models.ForeignKey(Cluster,related_name='reviews')
    text = models.CharField(max_length=255)
    data = models.CharField(max_length=255)



