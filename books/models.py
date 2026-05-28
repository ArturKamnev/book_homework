from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название книги")
    author = models.CharField(max_length=50, verbose_name="Автор книги")
    genre = models.CharField(max_length=20, verbose_name="Жанр книги")
    description = models.TextField(verbose_name="Описание книги")
    publication_year = models.PositiveIntegerField(verbose_name="Год издания книги")
    pages = models.PositiveIntegerField(verbose_name="Количество страниц в книге")
    publisher = models.CharField(max_length=50, verbose_name="Издательство книги")
    rating = models.DecimalField(verbose_name="Рейтинг книги", max_digits=2, decimal_places=1)
    cover = models.ImageField(upload_to='books/', verbose_name="Обложка книги", blank=True)
    reservation_limit = models.PositiveSmallIntegerField(default=1, validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ])
    

    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f"{self.author} - {self.title}"