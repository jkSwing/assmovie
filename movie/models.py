from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100)
    onshow = models.BooleanField()
    wanted = models.IntegerField()
    show_time = models.DateField()
    poster_img = models.CharField(max_length=255)

    class Meta:
        db_table = 'movie'

    def __str__(self):
        return self.name


class Cinema(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'cinema'

    def __str__(self):
        return self.name


class ShowRecord(models.Model):
    cinema = models.ForeignKey(Cinema, models.CASCADE)
    time = models.DateTimeField()
    room = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, models.CASCADE)

    class Meta:
        db_table = 'show_record'


class Actor(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'actor'

    def __str__(self):
        return self.name


class ActorMovie(models.Model):
    actor = models.ForeignKey(Actor, models.CASCADE)
    movie = models.ForeignKey(Movie, models.CASCADE, related_name='actors')

    class Meta:
        db_table = 'actor_movie'

    def __str__(self):
        return str(self.actor)


class RateRecord(models.Model):
    user = models.ForeignKey('user.User', models.DO_NOTHING)
    movie = models.ForeignKey(Movie, models.CASCADE)
    score = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        db_table = 'rate_record'
