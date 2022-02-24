from rest_framework.serializers import ModelSerializer
from .models import Movie , Video


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'genre',
                  'rating', 'type', 'flyer', 'age_limit']


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = ['id','title','description','movie','videofile']