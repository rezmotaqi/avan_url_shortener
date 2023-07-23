from rest_framework import serializers

from url_shortener_project.settings import MAIN_DOMAIN
from .models import Url


class UrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = Url
        fields = ['short_url', 'long_url']
        read_only_fields = ['short_url',]

    def to_representation(self, instance):
        data = super(UrlSerializer, self).to_representation(instance)
        data["short_url"] = f"{MAIN_DOMAIN}{data.get('short_url')}"
        return data

