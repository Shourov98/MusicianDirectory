from django.db import models

# Create your models here.

class Musician(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    instrument_type = models.CharField(max_length=40)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
class Album(models.Model):
    name = models.CharField(max_length=30)
    musician = models.ManyToManyField(Musician)
    release_date = models.DateTimeField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return self.name
    
