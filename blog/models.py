from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


# Create your models here.
class PostCategory(models.Model):
    cat_title       = models.CharField(max_length=200)
    cat_desc        = models.TextField()

    def __str__(self):
        return self.cat_title

class Post(models.Model):
    title           = models.CharField(max_length=200)
    slug            = models.SlugField(null=True)
    content         = models.TextField()
    date_posted     = models.DateTimeField(default=timezone.now)
    thumb           = models.ImageField(default='default.png', blank=True, upload_to='images/')
    author          = models.ForeignKey(User, on_delete=models.CASCADE)
    fetured         = models.BooleanField(default=False)
    published       = models.BooleanField(default=False)
    cat             = models.ForeignKey(PostCategory, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'slug': self.slug})

@receiver(pre_save, sender=Post)
def pre_save_slug(sender, **kwargs):
    slug = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug