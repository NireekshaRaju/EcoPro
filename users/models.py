from django.db import models

class users(models.Model):
    role_choices= [
        ('customer', 'customer'),
        # ('suppliers','suppliers'),
        ('admin','admin'),
    ]
    
    user_name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    phoneno =models.IntegerField()
    role=models.CharField(max_length=200, choices=role_choices, default='customer')

    

    def __str__(self) -> str:
        return self.user_name
