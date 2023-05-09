from rest_framework import serializers
from mo.models import City, Posylka

class CitySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)


class PosylkaSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50, required=False)
    pos_id = serializers.CharField(max_length=50, required=False)
    status = serializers.BooleanField(required=False)
    cost = serializers.DecimalField(decimal_places=2, max_digits=25, required=False)
    weight = serializers.DecimalField(decimal_places=2, max_digits=25, required=False)
    date = serializers.DateField(required=False)
    
    class Meta:
        model = Posylka
        exclude = ['cityDestination', 'cityArrival']

class QuestionSerializer(serializers.Serializer):
    question = serializers.CharField(max_length=50)
    answer = serializers.CharField(max_length=50)

class UsersSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)