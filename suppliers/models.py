from django.db import models

class vendor(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    phoneno =models.IntegerField()

    def __str__(self) -> str:
        return self.name
