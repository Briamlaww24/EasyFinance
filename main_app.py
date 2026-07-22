import questionary, json
import pandas as pd 

datos = {
    'Fecha': ['2026-04-12', '2026-04-14', '2026-04-14', '2026-04-14'],
    'producto': ['laptop', 'monitor', 'teclado', ' mouse'],
    'precio': ['8','7', '5','9'],
    'cantidad':[2, 3, 4, 5]

}
df = pd.DataFrame(datos)
print(df)

ingreso_fecha = input("Ingrese la Fecha: ")
datos['Fecha'].append(ingreso_fecha)

ingreso_producto = input("Ingrese el producto: ")
datos['producto'].append(ingreso_producto)

ingreso_precio = input("Ingrese el precio: ")
datos['precio'].append(ingreso_precio)

ingreso_cantidad = input("Ingrese la Cantidad: ")
datos['cantidad'].append(ingreso_cantidad)

df = pd.DataFrame(datos)
print(df)

df.to_excel("archivo_pandas.xlsx", index=False, sheet_name="Datos")

