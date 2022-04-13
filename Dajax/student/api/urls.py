from django.urls import path, include
from rest_framework.routers import DefaultRouter
from student.api import views



router = DefaultRouter()

router.register('userapi',views.UserViewSet,basename='user')

urlpatterns = [

    path('',include(router.urls)),
       
]
