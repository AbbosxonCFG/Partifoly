from django.shortcuts import render
from .models import User
from .serializer import UserSerializer
from rest_framework  import generics
from rest_framework .response import Response
from rest_framework  import status


class Register(generics.GenericAPIView):
    serializer_class=UserSerializer

    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            contex={
                'massage':'User created succesfully',
                'data':serializer.data

            }

            return Response(data=contex,status=201)
        return Response(data=serializer.errors,status=400)
