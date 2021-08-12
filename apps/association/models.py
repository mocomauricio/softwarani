from django.db import models
from django.contrib.auth import get_user_model

import os
from uuid import uuid4

User = get_user_model()

# Create your models here.
def path_and_rename(instance, filename):
    path = 'imagenes'
    ext = filename.split('.')[-1]

    # set filename as random string
    filename = '{}.{}'.format(uuid4().hex, ext)

    # return the whole path to the file
    return os.path.join(path, filename)

def path_and_rename2(instance, filename):
    path = 'archivos'
    ext = filename.split('.')[-1]

    # set filename as random string
    filename = '{}.{}'.format(uuid4().hex, ext)

    # return the whole path to the file
    return os.path.join(path, filename)


class Partner(models.Model):
    class Meta:
        verbose_name = "Socio"
        verbose_name_plural = "Socios"
        ordering = ['first_name', 'last_name']

    first_name = models.CharField(
        verbose_name='nombres', 
        max_length=150, 
    )

    last_name = models.CharField(
        verbose_name='apellidos', 
        max_length=150, 
    )

    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        null=True, 
        blank=True
    )

    phone = models.CharField(
        verbose_name='teléfono',
        max_length=30,
        null=True, 
        blank=True
    )

    mobile = models.CharField(
        verbose_name='celular',
        max_length=30,
        null=True, 
        blank=True
    )

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return self.get_full_name()


POSITION_CHOICES=[
    (0, 'Presidente'),
    (1, 'Vicepresidente'),
    (2, 'Tesorero'),
    (3, 'Secretario'),
    (4, 'Miembro Vocal'),
    (5, 'Miembro Titular'),
    (6, 'Miembro Suplente'),
]


class Executive(models.Model):
    class Meta:
        verbose_name = "Comisión Directiva"
        verbose_name_plural = "Comisión Directiva"
        ordering = ['position']

    partner = models.ForeignKey(
        Partner, 
        verbose_name="socio",
        on_delete=models.CASCADE, 
        related_name="+"
    )
    
    position = models.PositiveSmallIntegerField(
        verbose_name="cargo",
        choices=POSITION_CHOICES
    )


class JobOffer(models.Model):
    class Meta:
        verbose_name = "Bolsa de Trabajo"
        verbose_name_plural = "Bolsa de Trabajo"
        ordering = ['-id']

    title = models.CharField(
        verbose_name='título',
        max_length=256
    )

    image = models.ImageField(
        verbose_name='imagen',
        upload_to=path_and_rename, 
        max_length=255, 
        null=True,
    )

    publication_date = models.DateTimeField(
        verbose_name='fecha de publicacion',
        auto_now_add=True,
        null=True
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        editable=False
    )

    def __str__(self):
        return self.title

class Message(models.Model):
    class Meta:
        verbose_name='Mensaje'
        verbose_name_plural='Mensajes'

    name = models.CharField(
        verbose_name='nombre', 
        max_length=150, 
    )

    email = models.EmailField(
        verbose_name='email',
        max_length=255
    )

    subject = models.CharField(
        verbose_name='asunto',
        max_length=256
    )

    message = models.TextField(
        verbose_name='mensaje',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        verbose_name='fecha de creacion',
        auto_now_add=True,
        null=True
    )


class Post(models.Model):
    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-publication_date']

    title = models.CharField(
        verbose_name='título',
        max_length=256
    )

    short_description = models.CharField(
        verbose_name='descripción corta',
        max_length=256
    )
    
    body = models.TextField(
        verbose_name='cuerpo'
    )
    
    publication_date = models.DateTimeField(
        verbose_name='fecha de publicacion',
        auto_now_add=True
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        editable=False
    )

    def __str__(self):
        return self.title

class File(models.Model):
    class Meta:
        verbose_name = "archivo"
        verbose_name_plural = "archivos"

    title = models.CharField(
        verbose_name='título',
        max_length=256
    )

    file = models.FileField(
        verbose_name='archivo',
        upload_to=path_and_rename2, 
        max_length=255, 
    )

    upload_date = models.DateTimeField(
        verbose_name='fecha de subida',
        auto_now_add=True
    )


    def __str__(self):
        return self.title


class Device(models.Model):
    class Meta:
        verbose_name = 'Dispositivo'
        verbose_name_plural = 'Dispositivos'

    token = models.TextField()
    active = models.BooleanField(verbose_name="activo" ,default=False)
    created_at = models.DateTimeField(verbose_name="fecha creación", auto_now_add=True)

    def __str__(self):
        return self.token 