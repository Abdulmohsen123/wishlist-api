from django.contrib.auth.models import User
from items.models import *
from rest_framework import serializers


class AddedBySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name",]

class ItemListSerializer(serializers.ModelSerializer):
    added_by = AddedBySerializer()
    wish_for = serializers.SerializerMethodField()
    detail = serializers.HyperlinkedIdentityField(
        view_name = "api-detail",
        lookup_field = "id",
        lookup_url_kwarg = "item_id"
)
    class Meta:
        model = Item
        fields = ['image', 'added_by', 'name', 'detail', 'wish_for','added_by']

    def get_wish_for(self,obj):
        return "wish for %s" % (obj.name)

class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"