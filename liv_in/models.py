from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
class HomeInfo(models.Model):
    House_number = models.CharField(max_length=5, unique=True, primary_key = True)
    House_Name = models.CharField(max_length=25, null = False)
    B_H_K = models.IntegerField()
    Rent = models.IntegerField()
    Location =  models.CharField(max_length=50)
    Sq_ft = models.IntegerField()
    Occupied = models.BooleanField()
    Place = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return self.House_number + ' ' + self.Place
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})