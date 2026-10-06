from django.db import models
from django.core.validators import MinValueValidator

class Medicamento(models.Model):
    nombre = models.CharField(max_length=120, verbose_name="Nombre Comercial")
    laboratorio = models.CharField(max_length=100)
    precio = models.IntegerField(
        validators=[MinValueValidator(1, message="El precio debe ser mayor a 0")]
    )
    stock = models.IntegerField(
        validators=[MinValueValidator(0, message="El stock no puede ser negativo")]
    )
    descripcion = models.TextField(blank=True, null=True)
    requiere_receta = models.BooleanField(default=False)
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} ({self.laboratorio})"