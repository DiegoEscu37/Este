from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify
################################
##### Modelo Perfil Usuario ####
################################


class Perfil(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='perfil', verbose_name='Usuario')
    imagen = models.ImageField(
        upload_to='usuarios/avatar/', null=True, blank=True, default='usuarios/avatar/default_user.png')
    telefono = models.CharField(max_length=30, null=True,
                                blank=True, verbose_name='Teléfono')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-id']

    def __str__(self):
        return self.username


###########################
##### Modelo Acerca de ####
###########################

class Acerca(models.Model):
    descripcion = models.CharField(max_length=450, verbose_name='Descripción')
    creacion = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación')
    actualizacion = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Acerca de'
        verbose_name_plural = 'Acerca de nosotros'
        ordering = ['-creacion']

    def __str__(self):
        return self.descripcion

################################
##### Modelo Redes Sociales ####
################################


class Red(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Red Social')
    url = models.URLField(max_length=300, null=True,
                          blank=True, verbose_name='Enlace')
    icono = models.CharField(max_length=150, null=True,
                             blank=True, verbose_name='Icono')
    creacion = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación')
    actualizacion = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


###########################
##### Modelo Categoria ####
###########################

class Categoria(models.Model):
    nombre = models.CharField(
        max_length=200, unique=True, verbose_name='Nombre')
    slug = models.SlugField()
    activo = models.BooleanField(default=True, verbose_name='Activo')
    creacion = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación')
    actualizacion = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Categoria, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre


##########################
##### Modelo Etiqueta ####
##########################

class Etiqueta(models.Model):
    nombre = models.CharField(
        max_length=200, unique=True, verbose_name='Nombre')
    activo = models.BooleanField(default=True, verbose_name='Activo')
    creacion = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación')
    actualizacion = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


##########################
#### Modelo Artículos ####
##########################

class Articulo(models.Model):
    titulo = models.CharField(
        max_length=250, unique=True, verbose_name='Título')
    slug = models.SlugField()
    bajada = models.CharField(max_length=150, verbose_name='Bajada')
    contenido = RichTextField(verbose_name='Contenido')
    imagen = models.ImageField(
        upload_to='blog/articulos/imagenes', null=True, blank=True, verbose_name='Imagen')
    publicado = models.BooleanField(default=False, verbose_name='Publicado')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL,
                                  related_name='get_articulos', null=True, blank=True, verbose_name='Categoría')
    autor = models.ForeignKey(User, on_delete=models.SET_NULL,
                              related_name='get_articulos', null=True, blank=True, verbose_name='Autor')
    etiquetas = models.ManyToManyField(Etiqueta, verbose_name='Etiquetas')
    creacion = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación')
    actualizacion = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-creacion']

    def delete(self, using=None, keep_parents=False):
        self.imagen.delete(self.imagen.name)
        return super().delete()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Articulo, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo


class Comment(models.Model):    
    articulo = models.ForeignKey(Articulo,on_delete=models.CASCADE,related_name='comments')    
    usuario = models.CharField(max_length=100)
    # models.ForeignKey(User, on_delete=models.SET_NULL,
    #                           null=True, blank=True, verbose_name='Usuario')  
    email = models.EmailField()    
    contenido = models.TextField()    
    creacion = models.DateTimeField(auto_now_add=True) 
    actualizacion = models.DateTimeField(auto_now=True)   
    activo = models.BooleanField(default=True)   

    class Meta:        
        ordering = ['creacion']
        # indexes = [
        #     models.Index(fields=['created']),
        # ]  

    def __str__(self):
        return f'Comment by {self.usuario} on {self.articulo}'
        pass
    
    pass
