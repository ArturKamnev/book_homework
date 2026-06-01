from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    description = models.TextField(verbose_name="Описание категории", max_length=300)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
    
class Horse(models.Model):
    name = models.TextField(verbose_name="Кличка лошади", max_length=50)
    breed = models.TextField(verbose_name="Порода лошади", max_length=50)
    age = models.PositiveIntegerField(verbose_name="Возраст лошади")
    description = models.CharField(verbose_name="Описание лошади", max_length=300)
    photo = models.ImageField(upload_to="horses/", blank=True, verbose_name="Изображение лошади")

    def __str__(self):
        return f"{self.name} - {self.age}"
    
    class Meta:
        verbose_name = 'Лошадь'
        verbose_name_plural = 'Лошадей'
    

class Person(models.Model):
    name = models.TextField(verbose_name="Имя заказчика", max_length=30)
    surname = models.TextField(verbose_name="Фамилия заказчика", max_length=30)
    phone = models.CharField(verbose_name="Номер телефона заказчика")
    age = models.PositiveIntegerField(verbose_name="Возраст заказчика")
    horse = models.OneToOneField(Horse, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} {self.surname} - {self.phone}"

    class Meta:
        verbose_name = 'Клиента'
        verbose_name_plural = 'Клиентов'


class Tour(models.Model):
    title = models.TextField(verbose_name="Название тура")
    description = models.TextField(verbose_name="Описание тура")
    price = models.PositiveIntegerField(verbose_name="Цена тура")
    duration = models.CharField(verbose_name="Длительность тура")
    created_at = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.title} - {self.price} сом"
    
    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'

class Review(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='reviews')
    MARK = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    mark = models.CharField(max_length=100, choices=MARK, verbose_name="Оценка")
    text = models.TextField(blank=True, verbose_name="Описание к оценке")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.mark} - {self.text[0:10]}"
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

