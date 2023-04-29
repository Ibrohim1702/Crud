from rest_framework import serializers

from regis.models import Product


class CrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"