from .models import *
from rest_framework import serializers
from rest_framework .serializers import ModelSerializer



class CategorySerializer(ModelSerializer):
    class Meta:
        fields='__all__'
        model=Category


class BannerSerializer(ModelSerializer):
    class Meta:
        fields='__all__'
        model=Banner


class BookSerailizer(ModelSerializer):
    class Meta:
        fields='__all__'
        model=Book


class CourseSerializer(ModelSerializer):
    class Meta:
        fields='__all__'
        model=Course


class CoursePlaylistSerializer(ModelSerializer):
    class Meta:
        fields='__all__'
        model=Courseplaylist



class ReviewSerializer(ModelSerializer):
    class Meta:
        fields='__all__'
        model=Review

        # depth=1


class MentorSerializer(ModelSerializer):
    class Meta:
        model=Mentor
        fields='__all__'



class PaymentSerailizer(ModelSerializer):
    class Meta:
        model=Payment
        fields='__all__'
        

class CartSerializer(ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__'