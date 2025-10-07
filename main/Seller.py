
# Create your models here.
import uuid
from django.db import models
from django.contrib.auth.models import User

class Seller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    tanggallahir = models.DateField()
    email = models.EmailField(default=0)
    notelp = models.CharField(max_length=20)
    linksocmed = models.URLField(blank=True, null=True)
    password = models.CharField(max_length=255)


    
    def __str__(self):
        return self.name
    