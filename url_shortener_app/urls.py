from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("", views.convert_long_to_short_url),
    path("url_redirect/<str:url>", views.redirect_to_original_url),
]

app_name = 'url_shortener_app'
urlpatterns = format_suffix_patterns(urlpatterns)

