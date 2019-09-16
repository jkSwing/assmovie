from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from movie.models import Movie, ShowRecord, ActorMovie, RateRecord
from django.db.models import Avg


class MovieSerializer(ModelSerializer):
    cinema_num = serializers.SerializerMethodField()
    show_count = serializers.SerializerMethodField()
    # actors = serializers.SerializerMethodField()
    actors = serializers.StringRelatedField(many=True)
    score = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('id', 'name', 'onshow', 'wanted', 'show_time', 'poster_img', 'cinema_num', 'show_count', 'actors', 'score')

    def get_cinema_num(self, obj):
        return len(set(show_record.cinema_id for show_record in ShowRecord.objects.filter(movie_id=obj.id)))

    def get_show_count(self, obj):
        return ShowRecord.objects.filter(movie_id=obj.id).count()

    # def get_actors(self, obj):
    #     return list(actor_movie.actor.name for actor_movie in ActorMovie.objects.filter(movie_id=obj.id))

    def get_score(self, obj):
        tmp = RateRecord.objects.filter(movie_id=obj.id).aggregate(Avg('score'))
        return tmp['score__avg']


class ShowRecordSerializer(ModelSerializer):
    time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    movie = serializers.StringRelatedField()
    cinema = serializers.StringRelatedField()

    class Meta:
        model = ShowRecord
        fields = ('movie', 'cinema', 'time', 'room')
