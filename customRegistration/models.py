from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CustomUser(User):
    full_name = models.CharField(max_length=50, verbose_name='ФИО: ')
    phone_number = models.CharField(max_length=100, verbose_name="Номер телефона: ")
    date_of_birth = models.DateField()
    desired_position = models.CharField(max_length=100, verbose_name="Желаемая должность: ")
    education = models.CharField(max_length=50, verbose_name="Образование: ")
    work_experience = models.CharField(max_length=300, verbose_name="Опыт работы: ")
    skills = models.CharField(max_length=100, verbose_name="Навыки: ")
    resumes = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} - {self.phone_number}"