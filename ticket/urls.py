from django.urls import path
from ticket.views import get_tickets

ticket_urls = [
    path('', get_tickets),
]
