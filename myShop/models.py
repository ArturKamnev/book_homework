from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название категории")

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название продукта")
    price = models.PositiveIntegerField(verbose_name="Цена продукта")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return f"{self.name} - {self.category}"