import questionary
import pandas as pd
from datetime import date, datetime
from os import system
from time import sleep
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side

datos_excel = {
    'Fecha': [],
    'Producto': [],
    'Precio': [],
    'Cantidad': [],
    'Tipo': []
}

datos_utilidad = {
    'Ingresos Totales': [],
    'Egresos Totales': [],
    'Envíos Totales': [],
    'Utilidad Neta': []
}

fecha_actual = date.today().strftime("%Y/%m/%d")
fecha_actual2 = date.today().strftime("%Y-%m-%d")
Hora_actual = datetime.now().strftime("%H:%M:%S")
utililidad = 0.0

while True:
    system("clear")
    print("==================================================")
    print("|            BIENVENIDO A EASYFINANCE            |")
    print("==================================================")
    print("|                                                |")
    print("|           A continuacion seleccione            |")
    print("|           la opcion que desea realizar         |")
    print("|                                                |")
    print("==================================================")
    operaciones = questionary.select(
        "",
        instruction="(Use las flechas para moverse)",
        choices=[
            "> [Registrar ingreso]",
            "> [Registrar egreso]",
            "> [Registrar envío]",
            "> [Ver utilidad total]",
            "> [Reporte mensual]",
            "> [Salir]"
        ]
    ).ask()

    if operaciones == "> [Registrar ingreso]":
        system("clear")

        ingreso_fecha = fecha_actual
        datos_excel['Fecha'].append(ingreso_fecha)

        ingreso_producto = input("Ingrese el producto: ")
        datos_excel['Producto'].append(ingreso_producto)

        ingreso_precio = float(input("Ingrese el precio: "))
        datos_excel['Precio'].append(ingreso_precio)

        ingreso_cantidad = int(input("Ingrese la Cantidad: "))
        datos_excel['Cantidad'].append(ingreso_cantidad)

        datos_excel['Tipo'].append("+(Ingreso)")

        utililidad += (ingreso_precio * ingreso_cantidad)

        try:
            df = pd.read_excel("Reporte-EasyFinance.xlsx", sheet_name="Datos")

        except FileNotFoundError:
            df = pd.DataFrame(datos_excel)

        df = pd.concat([df, pd.DataFrame(datos_excel)], ignore_index=True)
        df.to_excel(f"Reporte-EasyFinance.xlsx", index=False, sheet_name="Datos")

    elif operaciones == "> [Registrar egreso]":
        system("clear")

        ingreso_fecha = fecha_actual
        datos_excel['Fecha'].append(ingreso_fecha)

        ingreso_producto = input("Ingrese el producto: ")
        datos_excel['Producto'].append(ingreso_producto)

        ingreso_precio = float(input("Ingrese el precio: "))
        datos_excel['Precio'].append(ingreso_precio)

        ingreso_cantidad = int(input("Ingrese la Cantidad: "))
        datos_excel['Cantidad'].append(ingreso_cantidad)

        datos_excel['Tipo'].append("-(Egreso)")

        try:
            df = pd.read_excel("Reporte-EasyFinance.xlsx", sheet_name="Datos")

        except FileNotFoundError:
            df = pd.DataFrame(datos_excel)

        df = pd.concat([df, pd.DataFrame(datos_excel)], ignore_index=True)
        df.to_excel(f"Reporte-EasyFinance.xlsx", index=False, sheet_name="Datos")

    elif operaciones == "> [Registrar envío]":
        system("clear")

        ingreso_fecha = fecha_actual
        datos_excel['Fecha'].append(ingreso_fecha)

        ingreso_producto = input("Ingrese el producto: ")
        datos_excel['Producto'].append(ingreso_producto)

        ingreso_precio = float(input("Ingrese el precio: "))
        datos_excel['Precio'].append(ingreso_precio)

        ingreso_cantidad = int(input("Ingrese la Cantidad: "))
        datos_excel['Cantidad'].append(ingreso_cantidad)

        datos_excel['Tipo'].append("-(Envío)")

        try:
            df = pd.read_excel("Reporte-EasyFinance.xlsx", sheet_name="Datos")

        except FileNotFoundError:
            df = pd.DataFrame(datos_excel)

        utililidad -= (ingreso_precio * ingreso_cantidad)

        df = pd.concat([df, pd.DataFrame(datos_excel)], ignore_index=True)
        df.to_excel(f"Reporte-EasyFinance.xlsx", index=False, sheet_name="Datos")

    elif operaciones == "> [Ver utilidad total]":
        system("clear")

        print("--------------------------------------------------")
        print("|                                                |")
        print(f"|   La utilidad total es: ${utililidad:.2f}      |")
        print("|                                                |")
        print("--------------------------------------------------")

    elif operaciones == "> [Reporte mensual]":
        system("clear")

        print("==================================================")
        print("|                                                |")
        print("|           A continuacion seleccione            |")
        print("|            Que mes desea visualizar            |")
        print("|                                                |")
        print("==================================================")
        system("xdg-open Reporte-EasyFinance.xlsx")

    elif operaciones == "> [Salir]":
        system("clear")
        print("==================================================")
        print("|                                                |")
        print("|          Gracias por usar EasyFinance          |")
        print("|                                                |")
        print("==================================================")
        sleep(2)
        quit()
