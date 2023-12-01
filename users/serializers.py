from rest_framework import serializers
from .models import Parent, Child

class ParentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Parent model.

    Includes a 'children' field representing the relationship with the Child model.
    The 'children' field lists the IDs of related Child instances.
    """
    children = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Parent
        fields = ['id', 'first_name', 'last_name', 'street', 'city', 'state', 'zip_code', 'children']


class ChildSerializer(serializers.ModelSerializer):
    """
    Serializer for the Child model.

    Serializes all fields of the Child model, including the foreign key reference to the Parent.
    """
    class Meta:
        model = Child
        fields = ['id', 'first_name', 'last_name', 'parent']
