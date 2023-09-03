from django.db import models


#superuser  user-gauravbhatt passwd-22558800

# Create your models here.


class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=10)
    desc=models.TextField()
    date=models.DateTimeField()

    def __str__(self):
        return f"Message from {self.name}"
    

    
