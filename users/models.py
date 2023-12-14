from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    cpf = models.CharField(max_length=11, unique=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    email = models.EmailField(unique=True, blank=False, null=False)
    
    USERNAME_FIELD = "email"  # ele usa por padrão o username
    REQUIRED_FIELDS = ['username'] 

    def __str__(self):
        return self.username
