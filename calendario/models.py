from django.db import models
from django.core.validators import FileExtensionValidator

class Nota(models.Model):
    mes = models.ForeignKey('Mes', related_name='notas', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Notas'
        ordering = ['fecha_creacion']

    def __str__(self):
        return f'Nota de {self.mes.nombre}: {self.titulo}'


class Mes(models.Model):
    MESES_CHOICES = [
        ('Marzo 2025', 'Marzo 2025'),
        ('Abril 2025', 'Abril 2025'),
        ('Mayo 2025', 'Mayo 2025'),
        ('Junio 2025', 'Junio 2025'),
        ('Julio 2025', 'Julio 2025'),
        ('Agosto 2025', 'Agosto 2025'),
        ('Septiembre 2025', 'Septiembre 2025'),
        ('Octubre 2025', 'Octubre 2025'),
        ('Noviembre 2025', 'Noviembre 2025'),
        ('Diciembre 2025', 'Diciembre 2025'),
        ('Enero 2026', 'Enero 2026'),
        ('Febrero 2026', 'Febrero 2026'),
    ]

    nombre = models.CharField(max_length=20, choices=MESES_CHOICES, unique=True)
    imagen_portada = models.ImageField(upload_to='portadas/', null=True, blank=True)
    mensaje = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Meses'
        ordering = ['fecha_creacion']

    def __str__(self):
        return self.nombre

class FotoMes(models.Model):
    mes = models.ForeignKey(Mes, related_name='fotos', on_delete=models.CASCADE)
    imagen = models.ImageField(
        upload_to='galeria/',
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])]
    )
    descripcion = models.CharField(max_length=200, blank=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Fotos del Mes'
        ordering = ['fecha_subida']

    def __str__(self):
        return f'Foto de {self.mes.nombre}'

class CancionMes(models.Model):
    mes = models.ForeignKey(Mes, related_name='canciones', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    archivo_mp3 = models.FileField(
        upload_to='canciones/',
        validators=[FileExtensionValidator(['mp3'])],
        null=True,
        blank=True
    )
    enlace_externo = models.URLField(blank=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Canciones del Mes'
        ordering = ['fecha_subida']

    def __str__(self):
        return f'Canción de {self.mes.nombre}: {self.titulo}'
