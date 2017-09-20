from datetime import date

from rest_framework import serializers

from datapoint.models import Datapoint


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
