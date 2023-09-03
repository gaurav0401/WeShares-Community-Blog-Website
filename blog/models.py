from django.db import models

# Create your models here.
# user- gauravblog
#pass - 22558800

class post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=122)
    content=models.CharField(max_length=5022)
    author=models.CharField(max_length=20)
    slug=models.CharField(max_length=120)
    date=models.DateTimeField()

    def __str__(self):
        return self.title + 'by' + self.author
    