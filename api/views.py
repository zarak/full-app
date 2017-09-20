# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group

from rest_framework import viewsets

from api.serializers import UserSerializer, GroupSerializer, DatapointSerializer
from api.models import Datapoint


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class DatapointViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows datapoints to be viewed or edited. Generate CRUD for Datapoint.
    """
    queryset = Datapoint.objects.all()
    serializer_class = DatapointSerializer
