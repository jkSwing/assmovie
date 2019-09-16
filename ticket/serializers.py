from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ticket.models import Ticket


class TicketSerializer(ModelSerializer):
    movie_id = serializers.IntegerField(source='show.movie.id')
    type = serializers.StringRelatedField()
    movie_name = serializers.StringRelatedField(source='show.movie')
    cinema_name = serializers.StringRelatedField(source='show.cinema')
    room = serializers.CharField(source='show.room')
    time = serializers.DateTimeField(source='show.time', format='%Y-%m-%d %H:%M')

    class Meta:
        model = Ticket
        fields = ('movie_id', 'cinema_name', 'movie_name', 'seat', 'type', 'price', 'room', 'time')
