# Generated by Django 4.2.4 on 2023-08-30 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siglas', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=100)),
                ('principio_activo', models.CharField(max_length=100)),
                ('proveedor', models.CharField(max_length=100)),
                ('laboratorio', models.CharField(max_length=100)),
                ('codigo', models.IntegerField()),
                ('unidades_paquete', models.IntegerField()),
                ('entrada_paquetes', models.IntegerField()),
                ('entrada_unidades', models.IntegerField()),
                ('salida_paquetes', models.IntegerField()),
                ('salida_unidades', models.IntegerField()),
                ('stock_final_paquetes', models.IntegerField()),
                ('stock_final_unidades', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_id', models.CharField(max_length=10)),
                ('tipo_id', models.CharField(max_length=2)),
                ('nombre', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=1)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=200)),
                ('documento_acudiente', models.CharField(max_length=10)),
                ('nombre_acudiente', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('modalidad', models.CharField(max_length=10)),
                ('edad', models.CharField(max_length=20)),
            ],
        ),
    ]
