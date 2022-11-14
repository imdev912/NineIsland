from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class Profile(models.Model):
    user = user = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile')
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_username()

    def save(self, *args, **kwargs):
        self.slug = "profile/" + slugify(self.user.get_username())
        super(Profile, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=256)
    thumbnail = models.ImageField(upload_to='category')
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = "category/" + slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Blog(models.Model):
    title = models.CharField(max_length=256)
    overview = CKEditor5Field('Overview', config_name='extends')
    content = CKEditor5Field('Content', config_name='extends')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog')
    thumbnail = models.ImageField(upload_to='blog')
    published = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    readtime = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)
