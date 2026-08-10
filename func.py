from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
import os
import time
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime, date
from pandas import DataFrame, read_excel, concat

###############################################################################
###############################################################################

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


###############################################################################
###############################################################################


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

def registrar_operacion_interfaz(tipo_operacion, descripcion, monto, cantidad, Usuario_actual, utililidad, utilidad_egresos, utilidad_envios, utlidad_total, Label_utlidad_total):

    datos_nuevos = {
    'Fecha': [],
    'Producto': [],
    'Precio': [],
    'Cantidad': [],
    'Tipo': []
    }

    fecha = date.today().strftime("%Y-%m-%d")
    datos_nuevos["Fecha"] = fecha

    producto = descripcion.get()
    datos_nuevos["Producto"] = producto

    precio = monto.get()
    datos_nuevos["Precio"] = precio

    cantidad_de_productos = cantidad.get()
    datos_nuevos["Cantidad"] = cantidad_de_productos

    tipo = tipo_operacion.get()
    datos_nuevos["Tipo"] = tipo

    if producto == "" or precio == "" or cantidad_de_productos == "" or tipo == "" :
        tk.messagebox.showerror("Error", "Ninguno de los campos debe estar vacio para poder registrar una operación")

    else:
        
        try:
            df = read_excel(f"Reporte-EasyFinance-{Usuario_actual}.xlsx", sheet_name="Datos")

        except FileNotFoundError:
            df = DataFrame(columns=["Fecha", "Producto", "Precio", "Cantidad", "Tipo"])

        df = concat([df, DataFrame([datos_nuevos])], ignore_index=True)
        df.to_excel(f"Reporte-EasyFinance-{Usuario_actual}.xlsx", index=False, sheet_name="Datos")

        formatear_excel(Usuario_actual)

        if tipo == "+(Ingreso)":
            resultado_utilidad = utililidad.get() + (float(precio) * int(cantidad_de_productos))
            utililidad.set(f"{resultado_utilidad:.2f}")
        elif tipo == "-(Egreso)":
            resultado_utilidad = utilidad_egresos.get() + (float(precio) * int(cantidad_de_productos))
            utilidad_egresos.set(f"{resultado_utilidad:.2f}")
        elif tipo == "-(Envio)":
            resultado_utilidad = utilidad_envios.get() + (float(precio) * int(cantidad_de_productos))
            utilidad_envios.set(f"{resultado_utilidad:.2f}")
        
        resultado_utilidad_total = utililidad.get() - (utilidad_egresos.get() + utilidad_envios.get())
        utlidad_total.set(f"{resultado_utilidad_total:.2f}")

        if utlidad_total.get() <= 0:
            Label_utlidad_total.configure(
                fg="#C0503B"
            )
        else:
            Label_utlidad_total.configure(
                fg="#3FA66B"
            )

        #####################################################################################

        limpiar_widgets(descripcion)
        limpiar_widgets(monto)
        limpiar_widgets(cantidad)
        # tipo_operacion.set("")

        #####################################################################################

        tk.messagebox.showinfo("Operacion Registrada", "Su operacion ha sido registrada correctamente en el sistema.")

    return utililidad, utilidad_egresos, utilidad_envios, utlidad_total

def limpiar_widgets(widget):
    widget.delete(0, "end")


def definir_color_botones_ingreso(tipo_operacion, registrar_ingreso, registrar_egreso, registrar_envio):
    if tipo_operacion.get() == "":
        registrar_ingreso.configure(bg="#1D7A6E")
        registrar_egreso.configure(bg="#1D7A6E")
        registrar_envio.configure(bg="#1D7A6E")

    elif tipo_operacion.get() == "+(Ingreso)":
        registrar_ingreso.configure(bg="#3FA66B")
        registrar_egreso.configure(bg="#1D7A6E")
        registrar_envio.configure(bg="#1D7A6E")

    elif tipo_operacion.get() == "-(Egreso)":
        registrar_egreso.configure(bg="#3FA66B")
        registrar_ingreso.configure(bg="#1D7A6E")
        registrar_envio.configure(bg="#1D7A6E")

    elif tipo_operacion.get() == "-(Envio)":
        registrar_envio.configure(bg="#3FA66B")
        registrar_ingreso.configure(bg="#1D7A6E")
        registrar_egreso.configure(bg="#1D7A6E")

def cargar_tabla_transacciones(Tree, Usuario):
    for item in Tree.get_children():
        Tree.delete(item)

    try:
        df = read_excel(f"Reporte-EasyFinance-{Usuario}.xlsx", sheet_name="Datos")

    except FileNotFoundError:
        df = DataFrame(columns=["Fecha", "Producto", "Precio", "Cantidad", "Tipo"])

    if df.empty:
        return

    for index, fila in df.iterrows():

        Tree.insert(
            "",
            "end",
            values=(
                fila["Fecha"],
                fila["Producto"],
                fila["Precio"],
                fila["Cantidad"],
                fila["Tipo"],
        
            ),
        )

def calcular_utilidades_totales(Usuario_actual, var_ingreso, var_egreso, var_envio, var_total, Label_utlidad_total):
    ingreso = 0
    egreso = 0
    envio = 0
    total = 0

    try:
        df = read_excel(f"Reporte-EasyFinance-{Usuario_actual}.xlsx", sheet_name="Datos")
    

        for index, item in enumerate(df["Tipo"]):
            if item == "+(Ingreso)":
                ingreso += df["Precio"][index] * df["Cantidad"][index]

        for index, item in enumerate(df["Tipo"]):
            if item == "-(Egreso)":
                egreso += df["Precio"][index] * df["Cantidad"][index]

        for index, item in enumerate(df["Tipo"]):
            if item == "-(Envio)":
                envio += df["Precio"][index] * df["Cantidad"][index]

        total = ingreso - (egreso + envio)

        var_ingreso.set(f"{ingreso:.2f}")
        var_egreso.set(f"{egreso:.2f}")
        var_envio.set(f"{envio:.2f}")
        var_total.set(f"{total:.2f}")

        if var_total.get() <= 0:
            Label_utlidad_total.configure(
                fg="#C0503B"
            )
        else:
            Label_utlidad_total.configure(
                fg="#3FA66B"
            )

        return var_ingreso, var_egreso, var_envio, var_total

    except:

        var_ingreso.set(0.00)
        var_egreso.set(0.00)
        var_envio.set(0.00)
        var_total.set(0.00)


def actualizar_hora(frame, label_hora):

    Actualizar_hora_actual = Obtener_fecha_actual()
    label_hora.config(text=Actualizar_hora_actual)
    frame.after(1000, actualizar_hora)

def logout(var_ingreso, var_egreso, var_envio, var_total):
    with open("recuerdame.txt", "w", encoding="utf-8") as f:
        olvidar = ""
        f.write(olvidar)

    var_ingreso.set("0.00")
    var_egreso.set("0.00")
    var_envio.set("0.00")
    var_total.set("0.00")

def exportar_reporte_en_excel(Usuario_actual):
    try:
        tk.messagebox.showinfo("Exportando Reporte", "El reporte de EasyFinance se exportara en su escritorio en formato excel (.xlsx)")
        os.system(f"cp Reporte-EasyFinance-{Usuario_actual}.xlsx ~/Escritorio/Reporte-EasyFinance-{Usuario_actual}.xlsx")
        os.system(f"xdg-open ~/Escritorio/Reporte-EasyFinance-{Usuario_actual}.xlsx")
    except FileNotFoundError:
        os.system(f"cp Reporte-EasyFinance-{Usuario_actual}.xlsx ~/Desktop/Reporte-EasyFinance-{Usuario_actual}.xlsx")
        os.system(f"xdg-open ~/Desktop/Reporte-EasyFinance-{Usuario_actual}.xlsx")


def calcular_Punto_Equilibrio(Usuario_actual):
    try:
        df = read_excel(f"Reporte-EasyFinance-{Usuario_actual}.xlsx", sheet_name="Datos")
    except FileNotFoundError:
        return None

    CF = 0
    ingresos_totales = 0
    unidades_vendidas = 0
    envios_totales = 0

    for index, item in enumerate(df["Tipo"]):
        if item == "-(Egreso)":
            CF += df["Precio"][index] * df["Cantidad"][index]

    for index, item in enumerate(df["Tipo"]):
        if item == "+(Ingreso)":
            ingresos_totales += df["Precio"][index] * df["Cantidad"][index]
            unidades_vendidas += df["Cantidad"][index]

    for index, item in enumerate(df["Tipo"]):
        if item == "-(Envio)":
            envios_totales += df["Precio"][index] * df["Cantidad"][index]

    if unidades_vendidas == 0:
        return None

    P = ingresos_totales / unidades_vendidas
    CV = envios_totales / unidades_vendidas

    if P <= CV:
        return {
            "Alcanzable": False,
            "P": P,
            "CV": CV,
            "CF": CF
        }

    x_equilibrio = CF / (P - CV)
    ingreso_equilibrio = P * x_equilibrio

    return {
        "Alcanzable": True,
        "X": x_equilibrio,
        "Ingreso": ingreso_equilibrio,
        "P": P,
        "CV": CV,
        "CF": CF
    }