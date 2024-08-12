# import asyncio
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .tasks import create_image_st_ai
# Create your views here.

from dcelery.settings import SECRET_KEY, STABILITY_API_KEY


@api_view(["POST"])
def get_image(request):
    if prompt := request.POST.get("prompt"):
        create_image_st_ai.delay(prompt)
        return Response(
            status=status.HTTP_200_OK,
            data={
                "message": "SUCCESS",
                }
        )
    else:
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={
                "message":"Please enter a valid prompt"
                },
        )