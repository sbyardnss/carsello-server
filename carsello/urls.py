"""
URL configuration for carsello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from carsello_api.views import ArtworkView, EventView, UserView, OrderView, login_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'artwork', ArtworkView, 'artwork')
router.register(r'events', EventView, 'event')
router.register(r'user', UserView, 'users')
router.register(r'orders', OrderView, 'order')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login_user),
    # path('send_email', send_email),
    path('', include(router.urls))
]
