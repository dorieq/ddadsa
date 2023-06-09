import json
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from mo.models import City, Posylka, Question, Users
from mo.serializers import CitySerializer, PosylkaSerializer, QuestionSerializer, UserSerializer

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
    

class UserViewSet(viewsets.ViewSet):
    queryset = Users.objects.all()

    def list(self, request):
        queryset = Users.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Users.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
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
        user = request.GET['user']
        queryset = Posylka.objects.filter(user_id=user)
        serializer = PosylkaSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Posylka.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PosylkaSerializer(user)
        return Response(serializer.data)

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

@csrf_exempt
def login(request):
    body = json.loads(request.body)
    login = body['login']
    password = body['password']
    search = Users.objects.filter(login=login, password=password).first()
    if not search:
        return JsonResponse({"Msg": "Bad Login or password"}, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'user': search.id})

@csrf_exempt
def create_order(request):
    body = json.loads(request.body)
    user = body['user']
    pos_id = body['pos_id']
    search = Users.objects.filter(id=user).first()
    pos = Posylka(
        user=search,
        pos_id=pos_id,
        status=False,
        cityArrival_id=1,
        cityDestination_id=1,
    )
    pos.save()
    return JsonResponse({'msg': "Ok"})


@csrf_exempt
def create_detailed_order(request):
    body = json.loads(request.body)
    user = body['user']
    pos_id = body['pos_id']
    city1 = body['city_destination']
    city2 = body['city_arrival']
    status = body['status']
    search = Users.objects.filter(id=user).first()
    pos = Posylka(
        user=search,
        pos_id=pos_id,
        status=status,
        cityArrival_id=city1,
        cityDestination_id=city2,
    )
    pos.save()
    return JsonResponse({'msg': "Ok"})

@csrf_exempt
def is_admin(request):
    body = json.loads(request.body)
    user = body['user']
    search = Users.objects.filter(id=user).first()
    return JsonResponse({'admin': search.is_admin})

@csrf_exempt
def change_order(request):
    body = json.loads(request.body)
    pos_id = body['pos_id']
    city1 = body['city_destination']
    city2 = body['city_arrival']
    statusq = body['status']
    weight = body['weight']
    query = Posylka.objects.filter(pos_id=pos_id).first()
    if not query:
        return JsonResponse({"Msg": "Not found"}, status=status.HTTP_400_BAD_REQUEST)
    cityD = City.objects.filter(id=city1).first()
    cityA = City.objects.filter(id=city2).first()
    query.cityDestination = cityD
    query.cityArrival = cityA
    query.status = statusq
    query.weight = weight
    query.save()
    return JsonResponse({'msg': "Ok"})