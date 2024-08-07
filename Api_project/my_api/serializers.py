from rest_framework import serializers
from Base.models import Item
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields='__all__'