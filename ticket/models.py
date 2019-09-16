from django.db import models


class TicketType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'ticket_type'

    def __str__(self):
        return self.name


class Ticket(models.Model):
    user = models.ForeignKey('user.User', models.CASCADE)
    seat = models.CharField(max_length=50)
    type = models.ForeignKey(TicketType, models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    show = models.ForeignKey('movie.ShowRecord', models.CASCADE)

    class Meta:
        db_table = 'ticket'
