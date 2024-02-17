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
    RATE_CHOICE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    rating = models.PositiveSmallIntegerField(choices=RATE_CHOICE)
    post = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name='ratings', verbose_name='rating')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')

    def __str__(self):
        return f'{self.rating} - {self.post}'
    
class Like(models.Model):
    post = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name='likes')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    like = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.post} liked by {self.author}'
    
class Bookmark(models.Model):
    post = models.ForeignKey(Auto, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    in_bookmarks = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.author} saved {self.post} in bookmark'