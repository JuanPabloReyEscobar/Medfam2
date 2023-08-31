# inventory/models.py
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ("Vacunas Niños", "Vacunas Niños"),
    ("Vacunas", "Vacunas"),
)


class UserProfile(models.Model):
    class Meta:
        app_label = 'inventory'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    physical_address = models.CharField(max_length=40, null=True)
    mobile = models.CharField(max_length=12, null=True)
    picture = models.ImageField(default="avatar.jpeg", upload_to="Pictures")

    def __str__(self) -> str:
        return self.user.username


class Product(models.Model):
    Siglas = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    cantidad = models.PositiveIntegerField(null=True)
    descripcion = models.CharField(max_length=200, null=True)
    principio_activo = models.CharField(max_length=200, null=True)
    proveedor = models.CharField(max_length=200, null=True)
    laboratorio = models.CharField(max_length=200, null=True)
    codigo = models.PositiveIntegerField( null=True)
    unidades_paquete = models.PositiveIntegerField( null=True)
    entrada_unidades = models.PositiveIntegerField( null=True)

    def __str__(self) -> str:
        return self.principio_activo


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.product} ordered quantity {self.order_quantity}"
    
    
    
class Paciente(models.Model):
    num_id = models.CharField(max_length=10)
    tipo_id = models.CharField(max_length=2)
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=1)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    documento_acudiente = models.CharField(max_length=10)
    nombre_acudiente = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    modalidad = models.CharField(max_length=10)
    edad = models.CharField(max_length=20)
    
    def __str__(self):
        return self.num_id
    
    
class Inventario(models.Model):
    siglas = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=100)
    principio_activo = models.CharField(max_length=100)
    proveedor = models.CharField(max_length=100)
    laboratorio = models.CharField(max_length=100)
    codigo = models.IntegerField()
    unidades_paquete = models.IntegerField()
    entrada_paquetes = models.IntegerField()
    entrada_unidades = models.IntegerField()
    salida_paquetes = models.IntegerField()
    salida_unidades = models.IntegerField()
    stock_final_paquetes = models.IntegerField()
    stock_final_unidades = models.IntegerField()

    def __str__(self):
        return self.siglas  # Cambia esto según cómo quieras que se muestre en las consultas
