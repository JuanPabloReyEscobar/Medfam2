# inventory/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from inventory.models import Product, Order, Inventario, Paciente


class UserRegistry(UserCreationForm):
    email = forms.EmailField()
    identificacion = forms.CharField(max_length=20) 

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "identificacion",
            "password1",
            "password2",
        ]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["Siglas", "category", "cantidad", "descripcion", "principio_activo", "proveedor", "laboratorio", "codigo", "unidades_paquete", "entrada_unidades"]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["product", "order_quantity"]
        
        
class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ["siglas", "descripcion", "principio_activo", "proveedor", "laboratorio", "codigo", "unidades_paquete", "entrada_unidades"]
        
        
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ["num_id", "tipo_id", "nombre", "genero", "fecha_nacimiento", "direccion", "documento_acudiente", "nombre_acudiente", "telefono", "modalidad", "edad"]