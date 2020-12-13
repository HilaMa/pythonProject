from django.urls import path
from .views import homepage_view
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')

urlpatterns = [
    #path('', homepage_view, name='homepage')
    url(r'^myapp_view/', views.HelloAPIView.as_view()),
    url(r'', include(router.urls))

]