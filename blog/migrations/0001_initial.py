# Generated by Django 3.2 on 2022-04-16 04:38

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('status', models.CharField(choices=[('0', 'draft'), ('1', 'published')], default='D', max_length=16, verbose_name='Blog Status')),
                ('date_published', models.DateTimeField(verbose_name='Published Date')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('dislikes', models.ManyToManyField(related_name='dislikes', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
                'ordering': ['-date_updated'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Tag Name')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='Reply Date')),
                ('body', models.CharField(max_length=512, verbose_name='Body')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reply',
                'verbose_name_plural': 'Replies',
                'ordering': ['-date_time'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Content')),
                ('image', models.ImageField(blank=True, null=True, upload_to=blog.models.get_post_image, verbose_name='Image')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.blog')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='Comment Date')),
                ('body', models.CharField(max_length=512, verbose_name='Body')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ['-date_time'],
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
