from django.contrib import admin
from mo.models import Posylka, City, Question, Users

admin.site.register(City)
admin.site.register(Question)
admin.site.register(Users)
admin.site.register(Posylka)