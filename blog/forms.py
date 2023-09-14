from django.forms import ModelForm
from blog.models import post

class PostForm(ModelForm):
    class Meta:
        model=post
        fields= ['content',]
