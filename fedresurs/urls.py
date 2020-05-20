from django.urls import path
from .views import *

urlpatterns = [
    path('', make_info),
    path('guid/<str:guid>', get_info),
]