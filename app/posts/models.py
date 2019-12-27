from django.db import models

# Create your models here.


class Post(models.Model):
    cover = models.ImageField(
        upload_to="posts/covers",
        null=True,
        verbose_name='Cover'
    )
    title = models.CharField(max_length=90, verbose_name='Título')
    slug = models.CharField(max_length=90, verbose_name='Slug')
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de publicación')
    modified = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de última modificación')
    summary = models.TextField(verbose_name='Resumen')
    body = models.TextField(verbose_name='Cuerpo')
    tags = models.ManyToManyField('posts.Tag', verbose_name='Etiquetas')
    active = models.BooleanField(default=True, verbose_name='Activo')
    views = models.IntegerField(default=0, verbose_name='Visitas')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:post_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name='Nombre')
    slug = models.CharField(max_length=20, verbose_name='Slug')
    posts = models.ManyToManyField('posts.Post', verbose_name='Posts')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'

    def get_absolute_url(self):
        return reverse("posts:tag", kwargs={"slug": self.slug})
