# Generated by Django 4.0.6 on 2022-08-14 06:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import review.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('img_url', models.URLField()),
                ('book_info', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('isbn', models.CharField(max_length=10, unique=True)),
                ('category', models.CharField(max_length=50)),
                ('pubdate', models.DateField()),
                ('publisher', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='Review title', max_length=50)),
                ('content', models.TextField(help_text='Review content')),
                ('status', models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private'), ('DELETED', 'Deleted')], default='PUBLIC', help_text='Review status', max_length=7)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Review created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Review updated_at')),
                ('book', models.ForeignKey(db_column='book_id', on_delete=django.db.models.deletion.CASCADE, related_name='book', to='review.book')),
                ('user', models.ForeignKey(db_column='user_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'review',
                'verbose_name_plural': 'reviews',
            },
        ),
        migrations.CreateModel(
            name='ReviewImg',
            fields=[
                ('review_img_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('img', models.ImageField(null=True, upload_to=review.models.ReviewImg.review_img_upload_to)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('DELETED', 'Deleted')], default='ACTIVE', help_text='Review_img status', max_length=7)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Review_img created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Review_img updated_at')),
                ('review_id', models.ForeignKey(db_column='review_id', on_delete=django.db.models.deletion.CASCADE, to='review.review')),
            ],
            options={
                'verbose_name': 'reveiw_img',
                'verbose_name_plural': 'review_imgs',
            },
        ),
    ]
