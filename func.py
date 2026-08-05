from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
import questionary
import random
import os
import time
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from pandas import DataFrame, read_excel, concat

def main_login():
    while True: 
        print("Bienvenido desea crear una cuenta o logearse en una existente)?")
        respueta = questionary.select(
            message="",    
            instruction="(Usa las flechas)",
            choices=[
                "Iniciar Sesion",
                "Registrarme",
                "Salir"
            ],
        ).ask()

        registro = ""
        if respueta == "Iniciar Sesion" :
            usr = input("Ingrese su nombre de usuario: ")
            passwd = input("Ingrese su contraseña: ")
            Sesion = (f"{usr},{passwd}")
            with open("base_de_datos.txt", "r") as f:
                lectura = f.read()
            if Sesion in lectura :
                print("Bienvenido al systema")
                time.sleep(1)
                break
            else: 
                print("Error")

        elif respueta == "Registrarme" :
            usr2 = input("Ingrese el nombre de usuario a registrar: ")
            passwd2 = input("Ingrese su contraseña: ")
            registro = (f"{usr2},{passwd2}")
            with open("base_de_datos.txt", "a", encoding="utf-8") as f:
                f.write(registro+"\n")

        elif respueta == "Salir":
            quit()
    return usr

def formatear_excel(Usuario_actual):

    Excel = load_workbook(f"Reporte-EasyFinance-{Usuario_actual}.xlsx")
    hoja = Excel["Datos"]

    color_fondo = PatternFill(
        fill_type="solid",
        fgColor="81c9fa"
    )   

    for celda in hoja[1]:
        celda.font = Font(bold=True, color="FFFFFF")
        celda.fill = color_fondo
        celda.alignment = Alignment(horizontal="center")

    Excel.save(f"Reporte-EasyFinance-{Usuario_actual}.xlsx")

def login_interfaz(user, passwd):

    Usuario = user.get()
    Contraseña = passwd.get()
    Sesion = (f"{Usuario},{Contraseña}")
    with open("base_de_datos.txt", "r") as f:
        lectura = f.read()
    if Sesion in lectura :
        print("Bienvenido al systema")
        from Interfaz import Mostrar_ventana_principal
        Mostrar_ventana_principal()
    else: 
        print("Error")
        tk.messagebox.showerror("Error", "Usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.")


def registro_interfaz(user, passwd):

    Usuario = user.get()
    Contraseña = passwd.get()
    registro = (f"{Usuario},{Contraseña}")
    with open("base_de_datos.txt", "a", encoding="utf-8") as f:
        f.write(registro+"\n")

    tk.messagebox.showinfo("Operacion Completada", "Su cuenta ha sido registrada correctamente. Continue a iniciar sesión.")

def Obtener_fecha_actual():
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }

    fecha_actual = datetime.now()
    dia = fecha_actual.day
    mes = meses[fecha_actual.month]
    anio = fecha_actual.year

    formateo_fecha = f"{dia} de {mes} de {anio}"
    return formateo_fecha

def registrar_operacion_interfaz(fecha, tipo_operacion, descripcion, monto, cantidad, Usuario_actual, utililidad):

    datos_nuevos = {
    'Fecha': [],
    'Producto': [],
    'Precio': [],
    'Cantidad': [],
    'Tipo': []
    }

    datos_nuevos["Fecha"] = fecha

    producto = descripcion.get()
    datos_nuevos['Producto'] = producto

    precio = monto.get()
    datos_nuevos['Precio'] = precio

    cantidad_de_productos = cantidad.get()
    datos_nuevos['Cantidad'] = cantidad_de_productos

    tipo = tipo_operacion.get()
    datos_nuevos['Tipo'] = tipo

    if producto == "" or precio == "" or cantidad_de_productos == "" or tipo == "" :
        tk.messagebox.showerror("Error", "Ninguno de los campos debe estar vacio para poder registrar una operación")

    else:

        utililidad += (float(precio) * int(cantidad_de_productos))

        try:
            df = read_excel(f"Reporte-EasyFinance-{Usuario_actual}.xlsx", sheet_name="Datos")

        except FileNotFoundError:
            df = DataFrame(columns=["Fecha", "Producto", "Precio", "Cantidad", "Tipo"])

        df = concat([df, DataFrame([datos_nuevos])], ignore_index=True)
        df.to_excel(f"Reporte-EasyFinance-{Usuario_actual}.xlsx", index=False, sheet_name="Datos")

        formatear_excel(Usuario_actual)

    limpiar_widgets(descripcion)
    limpiar_widgets(monto)
    limpiar_widgets(cantidad)
    tipo_operacion.set("")

    return utililidad

def limpiar_widgets(widget):
    widget.delete(0, "end")