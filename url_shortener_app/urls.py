from django.urls import path
from . import views


urlpatterns = [
    path("", views.add_long_url, name="Add long(original url) and get short url"),
    path(
        "",
        views.get_short_url,
        name="Redirect to original_url which is retrieved by GET request based provided short url."
             " redirect to {main_domain}{original_url}"
         ),

]

