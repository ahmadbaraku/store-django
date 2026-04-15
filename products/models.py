from django.db import models

# Create your models here.
class product(models.Model):
    pro_name = models.CharField(max_length=255, unique=True)
    pro_price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='imgd', null=True)
