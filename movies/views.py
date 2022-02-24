from django.http import Http404
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Movie , Video 
from users.models import Profile
from .serializers import MovieSerializer , VideoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# from rest_framework_simplejwt import JWTAuthentication
# Create your views here.


class MoviesList(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        print('OK')
        print("Request",request.GET.get('profileId'))
        profile = Profile.objects.get(id=request.GET.get('profileId'))
        movies = Movie.objects.filter(age_limit=profile.maturity_setting)
        
        if(request.GET.get('genre')!='undefined'):
            movies = movies.filter(genre=request.GET.get('genre'))
        if(request.GET.get('isNetflixOriginals')!='undefined'):
            movies = movies.filter(isNetflixOriginals=True if request.GET.get('isNetflixOriginals')=='true' else False)

        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request)
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetail(APIView):
    # permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        movie = self.get_object(pk)
        movie_videos = Video.objects.filter(movie=movie.id)
        print("hello",movie_videos)
        serializer = MovieSerializer(movie)
        video_serializer = VideoSerializer(movie_videos,many=True)
        return Response({'movie':serializer.data,'videos':video_serializer.data})


class VideoList(APIView):
    def get(self,pk,movieId):
        print(pk)
        videos = Video.objects.filter(movie=movieId)
        print(videos)