# Generated by Django 4.0.6 on 2022-07-25 07:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_slug_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=100, verbose_name='İçerik'),
        ),
    ]
