from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from .models import RoomType, Room, User
from .serializers import RoomTypeSerializer, RoomSerializer, UserSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# Create your views here.
class RoomTypeView(ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


# class RoomView(ModelViewSet):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer

class RoomView(GenericAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get(self,request):
        room_objs =  Room.objects.all()
        serializer = RoomSerializer(room_objs,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class RoomEditView(GenericAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get(self,request,pk):
        try:
            room_obj = Room.objects.get(id=pk)
        except:
            return Response('Data not found!')
        serializer = RoomSerializer(room_obj)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            room_obj = Room.objects.get(id=pk)
        except:
            return Response('Data not found!')
        serializer = RoomSerializer(room_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        try:
            room_obj = Room.objects.get(id=pk)
        except:
            return Response('Data not found!')
        room_obj.delete()
        return Response('Data deleted')

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def register(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('User created!')
        else:
            return Response(serializer.errors)
        
    def login(self,request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(username=email,password=password)

        if user == None:
            return Response('Invalid credentials!')
        else:
            token,_ = Token.objects.get_or_create(user=user)
            return Response(token)




