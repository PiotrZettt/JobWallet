from rest_framework import serializers
from records.models import PartInstance, Operation
from django.contrib.auth.models import User

""" User, Operation and PartInstance are the query sets which our API module will return.
the serializers below will make sure """

class UserSerializer(serializers.ModelSerializer):
    operations = serializers.PrimaryKeyRelatedField(many=True, queryset=Operation.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'operations']


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ['processed_part', 'operation_name', 'comments', 'operator', 'operation_status', 'date_signed']

        def perform_create(self, serializer):
            serializer.save(owner=self.request.user)


class PartInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartInstance
        fields = ['pk', 'part_origin', 'serial_number']

