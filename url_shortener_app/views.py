from django.shortcuts import redirect, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from url_shortener_app.models import Url
from url_shortener_app.serializers import UrlSerializer


@api_view(["GET"])
@permission_classes([IsAdminUser])
def redirect_to_original_url(request, url):
    if request.method == "GET":
        url_object = get_object_or_404(Url, short_url=url)
        original_url = url_object.long_url
        return redirect(original_url)


@api_view(["POST"])
@permission_classes([IsAdminUser])
def convert_long_to_short_url(request):

    if request.method == "POST":
        serializer = UrlSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
