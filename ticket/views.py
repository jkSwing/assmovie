from rest_framework.response import Response
from ticket.models import Ticket
from rest_framework.decorators import api_view
from ticket.serializers import TicketSerializer
from datetime import datetime


@api_view(['GET'])
def get_tickets(request):
    user_id = request.GET.get('user_id')
    expired = request.GET.get('expired')
    page = request.GET.get('page')
    limit = request.GET.get('limit')
    if not user_id:
        return Response({'success': False, 'message': '...'})

    if not page:
        page = 1
    if not limit:
        limit = 5
    page = int(page)
    limit = int(limit)
    start = (page - 1) * limit
    if not expired or expired.lower() == 'false':
        tickets = Ticket.objects.filter(user_id=user_id).order_by('show__time', 'id')[start: start + limit]
    else:
        tickets = Ticket.objects.filter(user_id=user_id, show__time__gte=datetime.now()).order_by('show__time', 'id')[start: start + limit]
    serializer = TicketSerializer(tickets, many=True)

    return Response({'success': True, 'message': '成功', 'data': serializer.data})
