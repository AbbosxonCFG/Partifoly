from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from .router import router
# router=DefaultRouter()
# router.register('book/',Book,basename='book')

# urlpatterns=router.urls

urlpatterns=[
    path('category/',category,name='category'),
    path('category_ped/',category_ped,name='category_ped'),
    path('banner/',banner,name='banner'),
    path('banner_ped/',banner_ped,name='banner_ped'),
]

urlpatterns+=router.urls