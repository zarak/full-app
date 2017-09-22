# -*- coding: utf-8 -*-
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets

from datapoint.serializers import DatapointSerializer
from datapoint.models import Datapoint


class DatapointViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows datapoints to be viewed or edited. Generate CRUD for Datapoint.
    """
    queryset = Datapoint.objects.all()
    serializer_class = DatapointSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filter_fields = '__all__'
    search_fields = ('name',)
    ordering = ('date',)
