from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название жанра')
    description = models.TextField(max_length=300, verbose_name="Описание жанра")

    def __str__(self):
        return self.title

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название фильма")
    genre = models.ManyToManyField(Genre)
    photo = models.ImageField(upload_to='movies/')
    description = models.TextField(max_length=300, verbose_name="Описание фильма")
    release_date = models.DateField(verbose_name='Дата релиза фильма')
    duration = models.PositiveIntegerField(verbose_name="Длительность фильма (в минутах)")
    language = models.CharField(verbose_name="Язык фильма", max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Рейтинг")
    trailer_url = models.URLField(blank=True, verbose_name="Ссылка на трейлер")
    age_rating = models.CharField(max_length=5, verbose_name="Возрастное ограничение")

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.place)
    
class VipPlace(models.Model):
    place = models.PositiveIntegerField(verbose_name="ВИП место")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.place)

class VipSeat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='vip_seats')
    seat_number = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.movie.title} - VIP место {self.seat_number}'


class VipReservation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    seat = models.OneToOneField(VipSeat, on_delete=models.CASCADE, related_name='reservation')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.seat}'