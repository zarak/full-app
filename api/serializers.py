from datetime import date

from django.contrib.auth.models import User, Group

from rest_framework import serializers

from api.models import Datapoint


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class DatapointSerializer(serializers.ModelSerializer):
    """
    Prepare data to be represented in API. Create or update instance based on serializer logic.
    """
    days_left = serializers.SerializerMethodField()

    class Meta:
        model = Datapoint
        fields = '__all__'

    def get_days_left(self, obj):
        """
        Logic for generating custom fields.
        """
        return str(obj.date - date.today())
