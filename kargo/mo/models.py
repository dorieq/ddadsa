import datetime
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50, help_text='Название города')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Users(models.Model):
    login = models.CharField(max_length=50, help_text='Логин')
    password = models.CharField(max_length=50, help_text='Пароль')
    name = models.CharField(max_length=50, help_text='Имя')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city', help_text='Город', null=True)
    is_admin = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name
    
class Posylka(models.Model):
    name = models.CharField(max_length=50, help_text='Название')
    pos_id = models.CharField(max_length=50, help_text='ID посылки')
    status = models.BooleanField(help_text='Статус посылки')
    cityDestination = models.ForeignKey(City, on_delete=models.CASCADE, related_name='destination', help_text='Город отправления')
    cityArrival = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrival', help_text='Город направления')
    cost = models.DecimalField(decimal_places=2, max_digits=25, default=0, help_text='Цена')
    weight = models.DecimalField(decimal_places=2, max_digits=25, default=0, help_text='Вес')
    date = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="client", help_text="Клиент", null=True)

    def __str__(self) -> str:
        return self.pos_id

    class Meta:
        verbose_name = 'Посылка'
        verbose_name_plural = 'Посылки'


class Question(models.Model):
    question = models.TextField(help_text='Вопрос')
    answer = models.TextField(help_text='Ответ')
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

