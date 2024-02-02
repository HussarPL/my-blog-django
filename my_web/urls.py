from django.urls import path
from my_web.views import index

urlpatterns = [
    path("list/", index)
]