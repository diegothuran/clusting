# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from .models import Clusterizacao, Cluster, Review
from .serializers import ClusterizacaoSerializer, ClusterSerializer, ReviewSerializer

class ClusterizacaoList(generics.ListCreateAPIView):
    queryset = Clusterizacao.objects.all()
    serializer_class = ClusterizacaoSerializer

class ClusterList (generics.ListCreateAPIView):
    queryset = Cluster.objects.all()
    serializer_class = ClusterSerializer

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer