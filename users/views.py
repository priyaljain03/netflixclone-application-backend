from email import message
import profile
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer, ProfileSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Profile
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Profile

# Create your views here.


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            profiles = Profile.objects.filter(user=request.user.id)
            serializer = ProfileSerializer(profiles, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        data = {"name":request.data["name"],"maturity_setting":request.data["maturity_setting"],"user":request.user.id}
        print(data)
        serializer = ProfileSerializer(data=data)
        if serializer.is_valid():
            newprofile = serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        try:
            profile = Profile.objects.get(pk=pk)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        try:
            profile = Profile.objects.get(pk=pk)
            data = request.data['data']
            profile.name = data['name']
            profile.maturity_setting = data['maturity_setting']
            profile.save()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)



# class BlackListTokenView(APIView):
#     permission_classes = [AllowAny]

#     def post(self,request):
#         try:
#             refresh_token = request.data['refresh_token']
#             print(refresh_token)
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response({'success':"Token successfully blacklisted"})
#         except Exception as e:
#             return Response(status=status.status.HTTP_400_BAD_REQUEST)