from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


class HealthCheck(APIView):
    def get(self, request):
        """
		
		"""
        return Response({"message": "Service Available"})


class Info(APIView):
    def get(self, request):
        """
		Returns API information
		"""
        return Response("hello there!")
