from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content= models.TextField()

    created_at = models.DateTimeField(auto_now_add=True) #생성될 때 시간저장
    updated_at = models.DateTimeField(auto_now=True) #최근 수정일

    