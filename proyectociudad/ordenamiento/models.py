from django.db import models

class Parroquia(models.Model):
    
    UBICACION_CHOICES = [
        ('norte', 'Norte'),
        ('sur', 'Sur'),
        ('este', 'Este'),
        ('oeste', 'Oeste'),
    ]
    
    TIPO_CHOICES = [
        ('urbana', 'Urbana'),
        ('rural', 'Rural'),
    ]
    
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=10, choices=UBICACION_CHOICES)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    
    def __str__(self):
        return self.nombre
    


class Barrio(models.Model):
    
    NUMERO_PARQUES_CHOICES = [
        (1, '1'), (2, '2'), (3, '3'),
        (4, '4'), (5, '5'), (6, '6'),
    ]
    
    nombre = models.CharField(max_length=100)
    numero_viviendas = models.IntegerField()
    numero_parques = models.IntegerField(choices=NUMERO_PARQUES_CHOICES)
    numero_edificios_residenciales = models.IntegerField()
    parroquia = models.ForeignKey(
        Parroquia,
        on_delete=models.CASCADE,
        related_name='barrios'
    )
    
    def __str__(self):
        return self.nombre
    


class PresidenteBarrio(models.Model):
    
    cedula = models.CharField(max_length=10, unique=True)
    nickname = models.CharField(max_length=50)
    edad = models.IntegerField()
    profesion = models.CharField(max_length=100)
    barrio = models.ForeignKey(
        Barrio,
        on_delete=models.CASCADE,
        related_name='presidentes'
    )
    
    def __str__(self):
        return f'{self.nickname} - {self.cedula}'
    