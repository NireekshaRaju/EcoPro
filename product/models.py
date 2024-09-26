from django.db import models
import PIL
# Create your models here.
class product(models.Model):
    product_name= models.CharField(max_length=100)
    price= models.DecimalField(decimal_places=2,max_digits=10)
    quantity= models.IntegerField()
    # add_image=models.ImageField()
    add_image = models.ImageField(default="",upload_to='products/photos/')
    

    def __str__(self) -> str:
        return self.product_name