
# Create your models here.
import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('boots', 'Football Boots'),
        ('ball', 'Football'),
        ('accessory', 'Accessories'),
        ('training', 'Training Equipment'),
        ('merch', 'Merchandise'),
    ]
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES,default='update')
    rating = models.IntegerField(default=0)
    item_views = models.PositiveIntegerField(default=0)
    
    is_featured = models.BooleanField(default=False)

    
    def __str__(self):
        return self.name
    
    @property
    def is_recommended(self):
        return self.rating > 4
        
    def increment_views(self):
        self.item_views += 1
        self.save()