from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator

# Create your models here.

class CustomUser(AbstractUser):
        email = models.EmailField(max_length=254,validators=[EmailValidator()])
        age = models.PositiveIntegerField(null=True, blank=True)
        contact = models.CharField(max_length=15)
        address = models.TextField(blank=False)
        status = models.CharField(max_length=20, choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'),('widowed', 'Widowed'),])
        

