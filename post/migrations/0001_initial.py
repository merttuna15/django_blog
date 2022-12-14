# Generated by Django 4.0.6 on 2022-07-22 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Başlık')),
                ('content', models.TextField(max_length=100, verbose_name='İçerik')),
                ('publishing_date', models.DateTimeField(auto_now_add=True, verbose_name='Yayınlanma Tarihi')),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
