from django.conf import settings
from django.shortcuts import redirect, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from url_shortener_app.models import Url
from url_shortener_app.serializers import UrlSerializer


@api_view(["GET"])
# @permission_classes([IsAdminUser])
def get_short_url(request):
    """
    Retrieve the Original URL from the Short URL.

    This view allows administrators to retrieve the original URL from the short URL code by making a GET request to the endpoint.
    The view is protected by the IsAdminUser permission, ensuring only administrators can access it.

    Parameters:
    ----------
    request : rest_framework.request.Request
        The HTTP request object containing the 'short_url' parameter representing the code for the shortened URL.

    Returns:
    --------
    rest_framework.response.Response
        - If the 'short_url' code is found in the database, the view redirects the user to the original long URL.
        - If the 'short_url' code is not found, a 404 Not Found response is returned.

    Example:
    --------
    GET /get_short_url/?short_url=abcdef

    Response:
    HTTP 302 Found (redirects to the original long URL)
    """
    if request.method == "GET":
        short_url = request.GET.get("short_url")
        url_object = get_object_or_404(Url, short_url=short_url)
        original_url = url_object.long_url
        return redirect(f"{settings.MAIN_DOMAIN}{original_url}")


@api_view(["POST"])
# @permission_classes([IsAdminUser])
def add_long_url(request, url):
    """
    Add Long URL to the URL Shortener.

    This view allows administrators to add long URLs to the URL shortener by making a POST request to the endpoint.
    The view is protected by the IsAdminUser permission, ensuring only administrators can access it.

    Parameters:
    ----------
    request : rest_framework.request.Request
        The HTTP request object containing the long URL data to be added.

    Returns:
    --------
    rest_framework.response.Response
        - If the request data is valid, a 204 No Content response is returned, indicating the URL addition was successful.
        - If the request data is invalid, a 400 Bad Request response is returned with the validation errors.

    Example:
    --------
    POST /add_long_url/
    {
        "long_url": "https://www.example.com/some/long/url"
    }

    Response:
    HTTP 204 No Content
    """
    if request.method == "POST":
        serializer = UrlSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
