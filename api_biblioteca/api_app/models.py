from django.db import models
class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True, editable=False, db_column='id_autor')
    nombre = models.CharField(max_length=100, db_column='nombre')
    apellido = models.CharField(max_length=100, db_column='apellido')
    biografia = models.TextField(blank=True, null=True, db_column='biografia')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    class Meta:
        db_table = 'autor'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'