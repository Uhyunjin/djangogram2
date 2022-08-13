from django.db import models
from djangogram.users import models as user_model

class TimeStampedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True

# Create your models here.
class Post(TimeStampedModel):
    author = models.ForeignKey(
                user_model.User, 
                null=True, 
                on_delete=models.CASCADE, 
                related_name='post_author'
                )
    image = models.ImageField(blank=False)
    caption = models.TextField(blank=False)
    image_likes = models.ManyToManyField(
        user_model.User, 
        blank=True,
        related_name='post_image_likes')

    def __str__(self):
        return f"{self.author}:{self.caption}"


class Comment(TimeStampedModel):
    author = models.ForeignKey(
                user_model.User, 
                null=True, 
                on_delete=models.CASCADE, 
                related_name='comment_author'
                )
    posts = models.ForeignKey(
                Post, 
                null=True, 
                on_delete=models.CASCADE, 
                related_name='comment_post'
                ) 
    contents = models.TextField(blank=True)