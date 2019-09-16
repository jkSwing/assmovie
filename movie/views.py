from rest_framework.response import Response
from movie.models import ShowRecord, Movie
from rest_framework.decorators import api_view
from movie.serializers import MovieSerializer


@api_view(['GET'])
def get_movies(request):
    page = request.GET.get('page')
    limit = request.GET.get('limit')
    begin = request.GET.get('begin')
    end = request.GET.get('end')
    if not begin or not end:
        return Response({'success': False, 'message': '...'})

    if not page:
        page = 1
    if not limit:
        limit = 5
    page = int(page)
    limit = int(limit)
    start = (page - 1) * limit
    movies = Movie.objects.filter(show_time__range=(begin, end)).order_by('show_time', 'id')[start: start + limit]
    serializer = MovieSerializer(movies, many=True)

    return Response({'success': True, 'message': '成功', 'data': serializer.data})
