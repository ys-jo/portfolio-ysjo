from django.urls import path
from . import views

# FBV CBV
# FBV (Function based view)
# CBV (Class based view)

urlpatterns = [
    path('', views.index),
]
