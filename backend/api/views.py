from django.shortcuts import render
from .serializers import ApiSerializer
from rest_framework import generics, request
from .models import Chore
from rest_framework.fields import CurrentUserDefault
from rest_framework.response import Response
# Create your views here.

class ChoreListCreate(generics.ListCreateAPIView):
    queryset = Chore.objects.all()
    serializer_class = ApiSerializer

    def list(self, request):
        queryset = Chore.objects.all()
        serializer = ApiSerializer(queryset, many=True)
        return Response(serializer.data)