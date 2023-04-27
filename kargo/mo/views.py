from rest_framework import viewsets
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from mo.models import City, Posylka, Question
from mo.serializers import CitySerializer, PosylkaSerializer, QuestionSerializer

class CityViewSet(viewsets.ViewSet):
    queryset = City.objects.all()

    def list(self, request):
        queryset = City.objects.all()
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = City.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CitySerializer(user)
        return Response(serializer.data)
    
    
class QuestionViewSet(viewsets.ViewSet):
    queryset = Question.objects.all()
    
    def list(self, request):
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Question.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = QuestionSerializer(user)
        return Response(serializer.data)
    

class PosylkaViewSet(viewsets.ViewSet):
    queryset = Posylka.objects.all()

    def list(self, request):
        queryset = Posylka.objects.all()
        serializer = PosylkaSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Posylka.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PosylkaSerializer(user)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = PosylkaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk, format=None):
        queryset = Posylka.objects.all()
        device = get_object_or_404(queryset, pk=pk)
        serializer = PosylkaSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def update(self, request, pk, format=None):
        queryset = Posylka.objects.all()
        device = get_object_or_404(queryset, pk=pk)
        serializer = PosylkaSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)