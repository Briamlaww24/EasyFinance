from questionary import select
from pandas import DataFrame, read_excel, concat
from datetime import date, datetime
from os import system
from time import sleep
from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from b_login import main_login
import func

system("clear")
Usuario_actual = main_login()

datos_nuevos = {
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
    operaciones = select(
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
        datos_nuevos['Fecha'] = ingreso_fecha

        ingreso_producto = input("Ingrese el producto: ")
        datos_nuevos['Producto'] = ingreso_producto

        ingreso_precio = float(input("Ingrese el precio: "))
        datos_nuevos['Precio'] = ingreso_precio

        ingreso_cantidad = int(input("Ingrese la Cantidad: "))
        datos_nuevos['Cantidad'] = ingreso_cantidad

        datos_nuevos['Tipo'] = "+(Ingreso)"

        utililidad += (ingreso_precio * ingreso_cantidad)

        try:
            df = read_excel(f"Reporte-EasyFinance-{Usuario_actual}.xlsx", sheet_name="Datos")

        except FileNotFoundError:
            df = DataFrame(columns=["Fecha", "Producto", "Precio", "Cantidad", "Tipo"])

        df = concat([df, DataFrame([datos_nuevos])], ignore_index=True)
        df.to_excel(f"Reporte-EasyFinance-{Usuario_actual}.xlsx", index=False, sheet_name="Datos")

        func.formatear_excel()
        
    elif operaciones == "> [Registrar egreso]":
        system("clear")

        ingreso_fecha = fecha_actual
        datos_nuevos['Fecha'] = ingreso_fecha

        ingreso_producto = input("Ingrese el producto: ")
        datos_nuevos['Producto'] = ingreso_producto

        ingreso_precio = float(input("Ingrese el precio: "))
        datos_nuevos['Precio'] = ingreso_precio

        ingreso_cantidad = int(input("Ingrese la Cantidad: "))
        datos_nuevos['Cantidad'] = ingreso_cantidad

        datos_nuevos['Tipo'] = "-(Egreso)"

        try:
            df = read_excel(f"Reporte-EasyFinance-{Usuario_actual}.xlsx", sheet_name="Datos")

        except FileNotFoundError:
            df = DataFrame(columns=["Fecha", "Producto", "Precio", "Cantidad", "Tipo"])

        df = concat([df, DataFrame([datos_nuevos])], ignore_index=True)
        df.to_excel(f"Reporte-EasyFinance-{Usuario_actual}.xlsx", index=False, sheet_name="Datos")

        func.formatear_excel()

    elif operaciones == "> [Registrar envío]":
        system("clear")

        ingreso_fecha = fecha_actual
        datos_nuevos['Fecha'] = ingreso_fecha

        ingreso_producto = input("Ingrese el producto: ")
        datos_nuevos['Producto'] = ingreso_producto

        ingreso_precio = float(input("Ingrese el precio: "))
        datos_nuevos['Precio'] = ingreso_precio

        ingreso_cantidad = int(input("Ingrese la Cantidad: "))
        datos_nuevos['Cantidad'] = ingreso_cantidad

        datos_nuevos['Tipo'] = "-(Envío)"

        try:
            df = read_excel(f"Reporte-EasyFinance-{Usuario_actual}.xlsx", sheet_name="Datos")

        except FileNotFoundError:
            df = DataFrame(columns=["Fecha", "Producto", "Precio", "Cantidad", "Tipo"])

        utililidad -= (ingreso_precio * ingreso_cantidad)

        df = concat([df, DataFrame([datos_nuevos])], ignore_index=True)
        df.to_excel(f"Reporte-EasyFinance-{Usuario_actual}.xlsx", index=False, sheet_name="Datos")

        func.formatear_excel()

    elif operaciones == "> [Ver utilidad total]":
        system("clear")

        print("--------------------------------------------------")
        print("|                                                |")
        print(f"|   La utilidad total es: {utililidad:.2f}$      |")
        print("|                                                |")
        print("--------------------------------------------------")
        input()

    elif operaciones == "> [Reporte mensual]":
        system("clear")

        print("==================================================")
        print("|                                                |")
        print("|           A continuacion seleccione            |")
        print("|            Que mes desea visualizar            |")
        print("|                                                |")
        print("==================================================")
        system(f"xdg-open Reporte-EasyFinance-{Usuario_actual}.xlsx")

    elif operaciones == "> [Salir]":
        system("clear")
        print("==================================================")
        print("|                                                |")
        print("|          Gracias por usar EasyFinance          |")
        print("|                                                |")
        print("==================================================")
        sleep(2)
        quit()
