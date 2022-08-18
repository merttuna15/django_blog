from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


def get_create_url():
    return reverse('post:create')


class Post(models.Model):
    user = models.ForeignKey('auth.User', verbose_name='Yazar', on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200, verbose_name="Başlık")
    content = RichTextField(max_length=1000, verbose_name="İçerik")
    publishing_date = models.DateTimeField(verbose_name="Yayınlanma Tarihi", auto_now_add=True)
    image = models.FileField(null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)

    class Meta:
        ordering = ['-publishing_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post:update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post:delete', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey('post.Post', related_name='comments', on_delete=models.CASCADE)

    name = models.CharField(max_length=200, verbose_name='başlık')
    content = models.TextField(verbose_name='Yorum')
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)



