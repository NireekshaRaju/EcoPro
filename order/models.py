from django.db import models

# Create your models here.
class cart(models.Model):
    
    name= models.CharField(max_length=100)
    email=models.CharField(max_length=200,  default='' )
    address= models.CharField(max_length=100)
    phoneno= models.IntegerField()
    

    def __str__(self) -> str:
        return self.name