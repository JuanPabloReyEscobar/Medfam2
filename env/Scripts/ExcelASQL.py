import pandas as pd
import os
import sys

# Agrega la ruta de la carpeta 'medfam' al sys.path
medfam_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(medfam_path)

# Ahora puedes importar el modelo 'Product' desde 'Inventori'
from IMS.inventory.models import Product

def import_data_from_excel():
    excel_file = 'MedFam_IPS_Vacunacion_DEF.xlsx'
    sheet_name = 'Inventario'

    df = pd.read_excel(excel_file, sheet_name=sheet_name)

    for _, row in df.iterrows():
        product = Product(
            siglas=row['Siglas'],
            descripcion=row['Descripcion'],
            principio_activo=row['Principio Activo'],
            proveedor=row['Proveedor'],
            laboratorio=row['Laboratorio'],
            codigo=row['Codigo'],
            unidades_paquete=row['Unidades Paquete'],
            entrada_paquetes=row['Entrada Paquetes'],
            entrada_unidades=row['Entrada Unidades']
        )
        product.save()  # Guarda el producto en cada iteración

if __name__ == '__main__':
    import_data_from_excel()
