"""kargo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from mo.views import CityViewSet, QuestionViewSet, PosylkaViewSet, UserViewSet, login, create_order, create_detailed_order, is_admin
from rest_framework.routers import DefaultRouter

cityRouter = DefaultRouter()
cityRouter.register(r'cities', CityViewSet)

questionRouter = DefaultRouter()
questionRouter.register(r'questions', QuestionViewSet)

posylkaRouter = DefaultRouter()
posylkaRouter.register(r'posylkas', PosylkaViewSet)

userRouter = DefaultRouter()
userRouter.register(r'users', UserViewSet)

urlpatterns = [
    url('', include(cityRouter.urls), name='city'),
    url('', include(questionRouter.urls), name='question'),
    url('', include(posylkaRouter.urls), name='posylka'),
    url('', include(userRouter.urls), name='user'),
    path('login', login),
    path('create_order/', create_order),
    path("create_detailed_order/", create_detailed_order),
    path("is_admin/", is_admin),
    path('admin/', admin.site.urls),
]