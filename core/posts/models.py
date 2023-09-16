from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
from html_sanitizer.django import get_sanitizer


class Tag(models.Model):
    caption = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=150)
    # excerpt = models.CharField(max_length=200)
    # image_name = models.CharField(max_length=100)
    # image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True, blank=True, null=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="author")
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug
        
        sanitizer = get_sanitizer()
        self.content = sanitizer.sanitize(self.content)

        super().save(*args, **kwargs)

    # explanation https://youtu.be/-s7e_Fy6NRU?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&t=1651
    # redirect here after create post
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})
