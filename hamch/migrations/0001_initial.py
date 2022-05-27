# Generated by Django 4.0.4 on 2022-05-27 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='カテゴリー名')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='投稿タイトル')),
                ('content', models.TextField(max_length=4000, verbose_name='投稿内容')),
                ('name', models.CharField(max_length=30, verbose_name='投稿者')),
                ('try_count', models.IntegerField(default=0, verbose_name='試したい数')),
                ('try_done_count', models.IntegerField(default=0, verbose_name='試した数')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='hamch.category')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255, verbose_name='コメント内容')),
                ('name', models.CharField(max_length=30, verbose_name='コメント者')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='hamch.post')),
            ],
        ),
    ]
