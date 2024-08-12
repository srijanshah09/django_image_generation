from django.urls import path
from .import views

urlpatterns = [
    path('get-image/', view=views.get_image, name="get_image")
]