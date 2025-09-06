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

class Editorial(models.Model):
    id_editorial = models.AutoField(primary_key=True, editable=False, db_column='id_editorial')
    nombre = models.CharField(max_length=150, db_column='nombre')
    direccion = models.CharField(max_length=200, db_column='direccion')
    telefono = models.CharField(max_length=20, db_column='telefono')

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        db_table = 'editorial'
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'

class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True, editable=False, db_column='id_libro')
    titulo = models.CharField(max_length=200, db_column='titulo')
    resumen = models.TextField(blank=True, null=True, db_column='resumen')
    isbn = models.CharField(max_length=20, unique=True, db_column='isbn')
    anio_publicacion = models.IntegerField(blank=True, null=True, db_column='anio_publicacion')
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE, db_column='id_autor')
    editorial = models.ForeignKey('Editorial', on_delete=models.CASCADE, db_column='id_editorial')

    def __str__(self):
        return self.titulo
    
    class Meta:
        db_table = 'libro'
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'


class Miembro(models.Model):
    id_miembro = models.AutoField(primary_key=True, editable=False, db_column='id_miembro')
    nombre = models.CharField(max_length=100, db_column='nombre')
    apellido = models.CharField(max_length=100, db_column='apellido')
    email = models.EmailField(max_length=150, unique=True, db_column='email')
    fecha_membresia = models.DateField(db_column='fecha_membresia')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = 'miembro'
        verbose_name = 'Miembro'
        verbose_name_plural = 'Miembros'