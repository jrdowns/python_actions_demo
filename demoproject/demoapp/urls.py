from django.urls import path
from .views import polo_view

urlpatterns = [
    path('', polo_view, name='polo'),
]
