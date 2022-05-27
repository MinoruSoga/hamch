from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='カテゴリー名')
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    subject = models.CharField(max_length=255, verbose_name='投稿タイトル')
    content = models.TextField(max_length=4000, verbose_name='投稿内容')
    name = models.CharField(max_length=30, verbose_name='投稿者')
    category = models.ForeignKey(Category, related_name='posts', null=True, on_delete=models.CASCADE)
    try_count = models.IntegerField(default=0, verbose_name='試したい数')
    try_done_count = models.IntegerField(default=0, verbose_name='試した数')
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    content = models.CharField(max_length=255, verbose_name='コメント内容')
    name = models.CharField(max_length=30, verbose_name='コメント者')
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
