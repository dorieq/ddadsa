import datetime
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Posylka(models.Model):
    name = models.CharField(max_length=50)
    pos_id = models.CharField(max_length=50)
    status = models.BooleanField()
    cityDestination = models.ForeignKey(City, on_delete=models.CASCADE, related_name='destination')
    cityArrival = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrival')
    cost = models.DecimalField(decimal_places=2, max_digits=25, default=0)
    weight = models.DecimalField(decimal_places=2, max_digits=25, default=0)
    date = models.DateField(default=datetime.date.today)


class Question(models.Model):
    question = models.TextField()
    answer = models.TextField()
