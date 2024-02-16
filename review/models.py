from django.db import models
from product.models import Auto
from django.contrib.auth import get_user_model

User = get_user_model()

class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name='comments', verbose_name='Пост')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f' comment from {self.author.name} to {self.post}'
    
class Rating(models.Model):
    rating = models.PositiveSmallIntegerField()
    post = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name='ratings', verbose_name='rating')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')

    def __str__(self):
        return f'{self.rating} - {self.post}'
    
class Like(models.Model):
    post = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name='likes')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f'{self.post} liked by {self.author}'