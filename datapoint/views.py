# -*- coding: utf-8 -*-

from rest_framework import viewsets

from datapoint.serializers import DatapointSerializer
from datapoint.models import Datapoint


class DatapointViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows datapoints to be viewed or edited. Generate CRUD for Datapoint.
    """
    queryset = Datapoint.objects.all()
    serializer_class = DatapointSerializer
