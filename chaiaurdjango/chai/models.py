from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPES_CHOICE = {
        {'ML','MASALA'},
        {'GF','ANKITA'},
    }
    name = models.CharField(max_length=100)
    image_field = models.ImageField(upload_to='chai/')
    date_added = models.DateTimeField(default=timezone.now)
    type= models.CharField(max_length=2,choices=CHAI_TYPES_CHOICE)