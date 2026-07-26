import questionary, json
import pandas as pd
from datetime import date, datetime
from os import system

datos_excel = {
    'Fecha': [],
    'producto': [],
    'precio': [],
    'cantidad':[]
}

fecha_actual = date.today()
Hora_actual = date.today().strftime("%H:%M:%S")
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
        datos_excel['producto'].append(ingreso_producto)

        ingreso_precio = float(input("Ingrese el precio: "))
        datos_excel['precio'].append(ingreso_precio)

        ingreso_cantidad = int(input("Ingrese la Cantidad: "))
        datos_excel['cantidad'].append(ingreso_cantidad)

        df = pd.DataFrame(datos_excel)
        print(df)
        input()

        utililidad += (ingreso_precio * ingreso_cantidad)

        df.to_excel(f"archivo_pandas_{fecha_actual}.xlsx", index=False, sheet_name="Datos")

    elif operaciones == "> [Registrar egreso]":
        system("clear")

        ingreso_fecha = fecha_actual
        datos_excel['Fecha'].append(ingreso_fecha)

        ingreso_producto = input("Ingrese el producto: ")
        datos_excel['producto'].append(ingreso_producto)

        ingreso_precio = float(input("Ingrese el precio: "))
        datos_excel['precio'].append(ingreso_precio)

        ingreso_cantidad = int(input("Ingrese la Cantidad: "))
        datos_excel['cantidad'].append(ingreso_cantidad)

        df = pd.DataFrame(datos_excel)
        print(df)
        input()
        utililidad -= (ingreso_precio * ingreso_cantidad)

        with open(f"archivo_pandas_{fecha_actual}.xlsx", "a", encoding="utf-8") as f :
            df.to_excel(f"archivo_pandas_{fecha_actual}.xlsx", index=False, sheet_name="Datos")

    elif operaciones == "> [Registrar envío]":
        system("clear")

        ingreso_fecha = fecha_actual
        datos_excel['Fecha'].append(ingreso_fecha)

        ingreso_producto = input("Ingrese el producto: ")
        datos_excel['producto'].append(ingreso_producto)

        ingreso_precio = float(input("Ingrese el precio: "))
        datos_excel['precio'].append(ingreso_precio)

        ingreso_cantidad = int(input("Ingrese la Cantidad: "))
        datos_excel['cantidad'].append(ingreso_cantidad)

        df = pd.DataFrame(datos_excel)
        print(df)
        input()

        utililidad -= (ingreso_precio * ingreso_cantidad)

        with open(f"archivo_pandas_{fecha_actual}.xlsx", "a", encoding="utf-8") as f :
            df.to_excel(f"archivo_pandas_{fecha_actual}.xlsx", index=False, sheet_name="Datos")

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

        mes_dic = datos_excel['Fecha']
        mes = datetime.strftime(mes_dic, "%Y-%m-%d").month
        print(f"El mes actual es: {mes}")
