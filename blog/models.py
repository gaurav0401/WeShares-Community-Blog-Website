from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

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
    

class  handleComments(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.CharField(max_length=255)
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    post =models.ForeignKey(post, on_delete=models.CASCADE)
    parent =models.ForeignKey('self', on_delete=models.CASCADE , null=True)
    timestamp=models.DateTimeField(default=now)
    def __str__(self):
        return self.comment[0:15]+ ".... by "+ self.user.username
    