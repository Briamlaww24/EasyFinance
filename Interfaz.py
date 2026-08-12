import os
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
import func as fc
from datetime import date
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np

#####################################################################################

def login_interfaz(user, passwd, recuerdame):

    usr = user.get()
    contraseña = passwd.get()
    usrcontr = (f"{usr},{contraseña}")

    usrFormatdo = ""
    pLetra = usr[0].upper()
    resto = usr[1:]
    usrFormatdo = pLetra + resto

    with open("basesdedatos/base_de_datos.txt", "r", encoding="utf-8") as lectarchvo:
        lectura = lectarchvo.read()

    if usrcontr in lectura :
        print("Bienvenido al systema")
        Mostrar_ventana_principal(usrFormatdo)

        if recuerdame.get():
            with open("basesdedatos/recuerdame.txt", "w", encoding="utf-8") as lectarchvo:
                lectarchvo.write(usrcontr)
        else:
            with open("basesdedatos/recuerdame.txt", "w", encoding="utf-8") as lectarchvo:
                lectarchvo.write("")

    else:
        print("Error")
        tk.messagebox.showerror("Error", "El Usuario o la contraseña son incorrectos. Por favor, inténtelo de nuevo.")

#####################################################################################

mainWindow = tk.Tk()
mainWindow.title("EasyFinance")
mainWindow.geometry("1500x800")
mainWindow.resizable(False, False)
mainWindow.configure(bg="#8FBC8F")

recuerdame = tk.BooleanVar(value=False)

def Mostrar_ventana_login():

    if os.path.exists("basesdedatos/recuerdame.txt"):
        with open("basesdedatos/recuerdame.txt", "r", encoding="utf-8") as lectarchvo:
            usrGuard = lectarchvo.read().strip()

        if usrGuard:
            with open("basesdedatos/base_de_datos.txt", "r", encoding="utf-8") as lectarchvo:
                lectura = lectarchvo.read()

            if usrGuard in lectura:
                usrFormtd = ""
                usrGuard = usrGuard.split(",")
                usrFinal = usrGuard[0]
                pLetra = usrFinal[0].upper()
                resto = usrFinal[1:]
                usrFormtd = pLetra + resto
                Mostrar_ventana_principal(usrFormtd)
                return

    for widget in mainWindow.winfo_children():
        widget.destroy()
    
    frameLogin = tk.Frame(
        mainWindow,
        bg="#F7F4EC",
        width=1000,
        height=800,
        borderwidth=0,
        highlightthickness=0
    )
    frameLogin.pack(

        fill="both", 
        expand=False,
        side="left"
    )

    imagen = Image.open("imagenes/login_ilustracion.png")
    imagen = imagen.resize((1000,800))
    imagenLogin = ImageTk.PhotoImage(imagen)

    labelImagen = tk.Label(frameLogin, image=imagenLogin)
    labelImagen.image = imagenLogin
    labelImagen.pack(pady=0)

    FrameBotones = tk.Frame(
        mainWindow,
        bg="#80ac8e",
        width=500,
        height=800,
        borderwidth=0,
        highlightthickness=0
    )
    FrameBotones.pack(
        fill="both",
        expand=False,
        side="right"
    )

    inicioSesion = tk.Label(
        FrameBotones,
        text="Inicio de Sesión",
        font=("Serif", 23, "bold"),
        bg="#80ac8e",
        fg="White"
    )
    inicioSesion.pack(pady=50, padx=127)

    textoSesion = tk.Label(
        FrameBotones,
        text="Ingrese su nombre de usuario:",
        font=("Serif", 15, "bold"),
        bg="#80ac8e",
        fg="#2E322E"
    )
    textoSesion.place(y=200, x=15)

    ingresoSesion = tk.Entry(
        FrameBotones,
        width=40,
        font=("Serif", 15, "bold"),
        bg="#F7F4EC",
        fg="#2E322E",
        relief="solid"
    )
    ingresoSesion.place(y=240, x=15)

    textoSesion = tk.Label(
        FrameBotones,
        text="Ingrese su contraseña:",
        font=("Serif", 15, "bold"),
        bg="#80ac8e",
        fg="#2E322E",
    )
    textoSesion.place(y=280, x=15)

    ingresoPasswd = tk.Entry(
        FrameBotones,
        show="#",
        width=40,
        font=("Serif", 15, "bold"),
        bg="#F7F4EC",
        fg="#2E322E",
        relief="solid"
    )
    ingresoPasswd.place(y=320, x=15)

    tk.Checkbutton(
        FrameBotones,
        variable=recuerdame,
        text="Recuerdame",
        font=("Serif", 12, "bold"),
        onvalue=1,
        offvalue=0,
        bg="#80ac8e",
        fg="#2E322E",
        relief="flat",
        borderwidth=0,
        highlightbackground="#80ac8e",
        highlightthickness=0
        
    ).place(y=360, x=15)

    botonIngresar = tk.Button(
        FrameBotones,
        text="Ingresar",
        font=("Serif", 15, "bold"),
        bg="#F7F4EC",
        fg="#2E322E",
        command=lambda:login_interfaz(ingresoSesion, ingresoPasswd, recuerdame),
        relief="raised",
    )
    botonIngresar.place(y=380, x=180)

    Logo = Image.open("imagenes/logo.png")
    Logo = Logo.resize((400, 188))
    finalLogo = ImageTk.PhotoImage(Logo)

    labelLogo = tk.Label(
        FrameBotones,
        image=finalLogo,
        bg="#80ac8e"
    )
    labelLogo.image = finalLogo
    labelLogo.place(y=440, x=50)

    Logo2 = Image.open("imagenes/logo.png")
    Logo2 = Logo.resize((200, 94))
    finalLogo2 = ImageTk.PhotoImage(Logo2)

    labelLogo2 = tk.Label(
        frameLogin,
        image=finalLogo2,
        bg="#92b89e"
    )
    labelLogo2.image =finalLogo2
    labelLogo2.place(x=2, y=2)

    No_tiene_cuenta = tk.Button(
        FrameBotones,
        text="  ¿No tiene cuenta?. Regístrese aquí  ",
        font=("Serif", 12, "bold"),
        bg="#80ac8e",
        fg="#2E322E",
        highlightthickness=1,
        highlightbackground="#2E322E",
        command=Mostrar_ventana_registro,
        relief="flat",
    )
    No_tiene_cuenta.place(y=750, x=100)

def Mostrar_ventana_registro():
    for widget in mainWindow.winfo_children():
            widget.destroy()   
    
    frameLogin = tk.Frame(
        mainWindow,
        bg="#F7F4EC",
        width=1000,
        height=800,
    )
    frameLogin.pack(

        fill="both", 
        expand=False,
        side="left"
    )

    imagen = Image.open("imagenes/login_ilustracion.png")
    imagen = imagen.resize((1000,800))
    imagenLogin = ImageTk.PhotoImage(imagen)

    labelImagen = tk.Label(frameLogin, image=imagenLogin)
    labelImagen.image = imagenLogin
    labelImagen.pack(pady=0)

    frameBotones = tk.Frame(
        mainWindow,
        bg="#80ac8e",
        width=500,
        height=800
    )
    frameBotones.pack(
        fill="both",
        expand=False,
        side="right"
    )

    inicioSesion = tk.Label(
        frameBotones,
        text="Registro de Usuario",
        font=("Serif", 23, "bold"),
        bg="#80ac8e",
        fg="White"
    )
    inicioSesion.place(y=50, x=100)

    textoSesion = tk.Label(
        frameBotones,
        text="Ingrese su nuevo usuario:",
        font=("Serif", 15, "bold"),
        bg="#80ac8e",
        fg="#2E322E"
    )
    textoSesion.place(y=200, x=15)

    ingresoSesion = tk.Entry(
        frameBotones,
        width=40,
        font=("Serif", 15, "bold"),
        bg="#F7F4EC",
        fg="#2E322E",
        relief="solid"
    )
    ingresoSesion.place(y=240, x=15)

    textoSesion = tk.Label(
        frameBotones,
        text="Cree una contraseña segura:",
        font=("Serif", 15, "bold"),
        bg="#80ac8e",
        fg="#2E322E"
    )
    textoSesion.place(y=280, x=15)

    ingresoPasswd = tk.Entry(
        frameBotones,
        show="#",
        width=40,
        font=("Serif", 15, "bold"),
        bg="#F7F4EC",
        fg="#2E322E",
        relief="solid"
    )
    ingresoPasswd.place(y=320, x=15)

    botonIngresar = tk.Button(
        frameBotones,
        text="Registrarme",
        font=("Serif", 15, "bold"),
        bg="#F7F4EC",
        fg="#2E322E",
        command=lambda: fc.registro_interfaz(ingresoSesion, ingresoPasswd)
    )
    botonIngresar.place(y=380, x=170)

    Logo = Image.open("imagenes/logo.png")
    Logo = Logo.resize((400, 200))
    finalLogo = ImageTk.PhotoImage(Logo)

    labelLogo = tk.Label(
        frameBotones,
        image=finalLogo,
        bg="#80ac8e"
    )
    labelLogo.image = finalLogo
    labelLogo.place(y=440, x=50)

    noCuenta = tk.Button(
        frameBotones,
        text="  ¿Ya tiene cuenta?. Inicie sesión aquí  ",
        font=("Serif", 12, "bold"),
        bg="#80ac8e",
        fg="#2E322E",
        highlightthickness=1,
        highlightbackground="#2E322E",
        command=Mostrar_ventana_login,
        relief="flat",
    )
    noCuenta.place(y=750, x=90)

varUtililidadTotal = tk.DoubleVar(value=0.00)
varUtililidadEnvios = tk.DoubleVar(value=0.00)
varUtililidadEgresos = tk.DoubleVar(value=0.00)
varUtililidad = tk.DoubleVar(value=0.00)

def Mostrar_ventana_principal(usrActual):

    for widget in mainWindow.winfo_children():
        widget.destroy()

    User = usrActual

    fechaActual = fc.Obtener_fecha_actual()
    fechaActualDos = date.today().strftime("%Y-%m-%d")
    
    imagen = Image.open("imagenes/_.png")
    imagen = imagen.resize((1500,800))
    imagenFondo = ImageTk.PhotoImage(imagen)

    labelImagen = tk.Label(mainWindow, image=imagenFondo)
    labelImagen.image = imagenFondo
    labelImagen.place(x=0, y=0)

    mainWindow.configure(bg="#F7F4EC")

    #####################################################################################

    frameMenu = tk.Frame(
        mainWindow,
        bg="#8FBC8F",
        width=100,
        height=800,
    )
    frameMenu.pack(
        fill="both", 
        expand=False,
        side="left"
    )

    # Boton de la Casa

    logoCasa = Image.open("imagenes/casa.png")
    logoCasa = logoCasa.resize((77, 77))
    logoCasaFond = ImageTk.PhotoImage(logoCasa)
    botonCasa = tk.Button(
        frameMenu,
        bg="#2E322E",
        image=logoCasaFond,
        relief="flat",
        command=lambda: Mostrar_ventana_principal(usrActual),
        highlightthickness=2,
        highlightbackground="#2E322E",
        activebackground="#8FBC8F"
    )
    botonCasa.image = logoCasaFond
    botonCasa.place(x=8, y=8)

    # Boton de los Graficos

    logoGrafico = Image.open("imagenes/graficos.png")
    logoGrafico = logoGrafico.resize((77, 77))
    logoGraficoFondo = ImageTk.PhotoImage(logoGrafico)
    botonGrafico = tk.Button(
        frameMenu,
        bg="#2E322E",
        image=logoGraficoFondo,
        relief="flat",
        command=lambda: Mostrar_ventana_graficos(usrActual),
        highlightthickness=2,
        highlightbackground="#2E322E",
        activebackground="#8FBC8F"
    )
    botonGrafico.image = logoGraficoFondo
    botonGrafico.place(x=8, y=98)

    # Boton del Logout

    logoLogout = Image.open("imagenes/logout.png")
    logoLogout = logoLogout.resize((77, 77))
    logoLogoutFondo = ImageTk.PhotoImage(logoLogout)
    botonLogout = tk.Button(
        frameMenu,
        bg="#8FBC8F",
        image=logoLogoutFondo,
        relief="flat",
        command=lambda: (fc.logout(varUtililidad, varUtililidadEgresos, varUtililidadEnvios, varUtililidadTotal), Mostrar_ventana_login()),
        highlightthickness=0,
        activebackground="#5E8A6E"
    )
    botonLogout.image = logoLogoutFondo
    botonLogout.place(x=8, y=710)

    #####################################################################################

    tk.Label(
        mainWindow,
        text=f"¡Bienvenido a EasyFinance!, {usrActual}",
        bg="#F7F4EC",
        fg="#2E322E",
        font=("Serif", 20, "bold")
    ).place(x=135, y=15)

    tk.Label(
        mainWindow,
        text=f"Asi va tu tienda hoy, {fechaActual}",
        bg="#F7F4EC",
        fg="#8A8F87",
        font=("Serif", 15, "bold")
    ).place(x=135, y=60)

    #####################################################################################
    
    # Frame de la Utilidad

    frameUtil = tk.Frame(
        mainWindow,
        bg="#8FBC8F",
        width=730,
        height=100
    )
    frameUtil.place(x=755, y=30)

    numUtil = tk.Frame(
        frameUtil,
        bg="#F7F4EC",
        width=170,
        height=80,
    )
    numUtil.place(x=10, y=10)

    tk.Label(
        numUtil,
        text="INGRESOS:",
        font=("Serif", 10, "bold"),
        fg="#8A8F87",
        bg="#F7F4EC"
    ).place(x=5, y=5)

    utilidadIngr = tk.Label(
        numUtil,
        textvariable=varUtililidad,
        font=("Serif", 20, "bold"),
        fg="#3FA66B",
        bg="#F7F4EC"
    )
    utilidadIngr.place(x=5, y=30)

    # Framde de los egresos

    numsUtilEgr = tk.Frame(
        frameUtil,
        bg="#F7F4EC",
        width=170,
        height=80,
    )
    numsUtilEgr.place(x=190, y=10)

    tk.Label(
        numsUtilEgr,
        text="EGRESOS:",
        font=("Serif", 10, "bold"),
        fg="#8A8F87",
        bg="#F7F4EC"
    ).place(x=5, y=5)

    utilEgr = tk.Label(
        numsUtilEgr,
        textvariable=varUtililidadEgresos,
        font=("Serif", 20, "bold"),
        fg="#C0503B",
        bg="#F7F4EC"
    )
    utilEgr.place(x=5, y=30)

    # Frame de los Envios

    numsUtilEnvios = tk.Frame(
        frameUtil,
        bg="#F7F4EC",
        width=170,
        height=80,
    )
    numsUtilEnvios.place(x=370, y=10)

    tk.Label(
        numsUtilEnvios,
        text="ENVÍOS:",
        font=("Serif", 10, "bold"),
        fg="#8A8F87",
        bg="#F7F4EC"
    ).place(x=5, y=5)

    UtilEnvios = tk.Label(
        numsUtilEnvios,
        textvariable=varUtililidadEnvios,
        font=("Serif", 20, "bold"),
        fg="#C98A2E",
        bg="#F7F4EC"
    )
    UtilEnvios.place(x=5, y=30)

    # Frame de la Utilidad Total

    numsUtilTot = tk.Frame(
        frameUtil,
        bg="#2E322E",
        width=170,
        height=80,
    )
    numsUtilTot.place(x=550, y=10)

    tk.Label(
        numsUtilTot,
        text="UTILIDAD NETA:",
        font=("Serif", 10, "bold"),
        fg="#8A8F87",
        bg="#2E322E"
    ).place(x=5, y=5)

    utilTotal = tk.Label(
        numsUtilTot,
        textvariable=varUtililidadTotal,
        font=("Serif", 20, "bold"),
        fg="#3FA66B",
        bg="#2E322E"
    )
    utilTotal.place(x=5, y=30)

    fc.calcular_utilidades_totales(usrActual, varUtililidad, varUtililidadEgresos, varUtililidadEnvios, varUtililidadTotal, utilTotal)

    #####################################################################################

    frameRegisOp = tk.Frame(
        mainWindow,
        bg="#8FBC8F",
        width=730,
        height=600
    )
    frameRegisOp.place(x=755, y=150)

    tk.Label(
        frameRegisOp,
        text="Llene los campos para registrar una operación:",
        font=("Serif", 15, "bold"),
        bg="#8FBC8F",
        fg="#2E322E"
    ).place(x=30, y=7)

    frameTipoOp = tk.Frame(
        frameRegisOp,
        bg="#F7F4EC",
        width=614,
        height=60
    )
    frameTipoOp.place(x=59, y=60)

    tipoOp = tk.StringVar()

    registrarIngr = tk.Button(
        frameTipoOp,
        text="Registrar Ingreso",
        font=("Serif", 15, "bold"),
        bg="#1D7A6E",
        fg="Black",
        activebackground="#3FA66B",
        relief="flat",
        highlightthickness=2,
        highlightbackground="#2E322E",
        command=lambda: setear_variable_tipo_operacion(tipoOp, "+(Ingreso)"),
    )
    registrarIngr.place(x=10, y=10)

    registrarEgr = tk.Button(
        frameTipoOp,
        text="Registrar Egreso",
        font=("Serif", 15, "bold"),
        bg="#1D7A6E",
        fg="Black",
        activebackground="#3FA66B",
        relief="flat",
        highlightthickness=2,
        highlightbackground="#2E322E",
        command=lambda: setear_variable_tipo_operacion(tipoOp, "-(Egreso)")
    )
    registrarEgr.place(x=220, y=10)

    registrarEnv = tk.Button(
        frameTipoOp,
        text="Registrar Envío",
        font=("Serif", 15, "bold"),
        bg="#1D7A6E",
        fg="Black",
        activebackground="#3FA66B",
        relief="flat",
        highlightthickness=2,
        highlightbackground="#2E322E",
        command=lambda: setear_variable_tipo_operacion(tipoOp, "-(Envio)")
    )
    registrarEnv.place(x=420, y=10)

    def setear_variable_tipo_operacion(operacion, tipo):
            operacion.set(tipo)
            fc.definir_color_botones_ingreso(tipoOp, registrarIngr, registrarEgr, registrarEnv)
    
    tk.Label(
        frameRegisOp,
        text="Pequeña Descripción: ",
        font=("Serif", 15, "bold"),
        bg="#8FBC8F",
        fg="#2E322E"
    ).place(x=59, y=140)

    Desc = tk.Entry(
        frameRegisOp,
        width=55,
        font=("Serif", 15, "bold"),
        bg="#F7F4EC",
        fg="#2E322E",
        relief="solid",
        highlightcolor="#0e7c66",
        highlightthickness=2,
    )
    Desc.place(x=59, y=180)

    tk.Label(
        frameRegisOp,
        text="Monto: ",
        font=("Serif", 15, "bold"),
        bg="#8FBC8F",
        fg="#2E322E"
    ).place(x=59, y=230)

    Monto = tk.Entry(
        frameRegisOp,
        width=15,
        font=("Serif", 15, "bold"),
        bg="#F7F4EC",
        fg="#2E322E",
        relief="solid",
        highlightcolor="#0e7c66",
        highlightthickness=2
    )
    Monto.place(x=59, y=270)

    tk.Label(
        frameRegisOp,
        text="Cantidad: ",
        font=("Serif", 15, "bold"),
        bg="#8FBC8F",
        fg="#2E322E"
    ).place(x=500, y=230)

    Cant = tk.Entry(
        frameRegisOp,
        width=15,
        font=("Serif", 15, "bold"),
        bg="#F7F4EC",
        fg="#2E322E",
        relief="solid",
        highlightcolor="#0e7c66",
        highlightthickness=2
    )
    Cant.place(x=500, y=270)

    tk.Label(
        frameRegisOp,
        text="______________________________________________________________________",
        font=("Serif", 15, "bold"),
        bg="#8FBC8F",
        fg="#2E322E"
    ).place(x=50, y=330)

    textoFecha = tk.Label(
        frameRegisOp,
        text=f"Nota: La operacion se registrara con la fecha actual. \n ({fechaActual})",
        font=("Serif", 15, "bold"),
        bg="#8FBC8F",
        fg="#2E322E",
    )
    textoFecha.place(x=100, y="377")
    textoFecha.after(1000, lambda: fc.actualizar_hora(textoFecha))

    RegisTodo = tk.Button(
        frameRegisOp,
        text="REGISTRAR",
        font=("Serif", 15, "bold"),
        width=54,
        bg="#00FF7F",
        fg="Black",
        activebackground="#C0503B",
        relief="flat",
        highlightthickness=2,
        highlightbackground="#2E322E",
        command=lambda: (fc.registrar_operacion_interfaz(tipoOp, Desc, Monto, Cant, User, varUtililidad, varUtililidadEgresos, varUtililidadEnvios, varUtililidadTotal, utilTotal), fc.cargar_tabla_transacciones(tabla, usrActual))
    )
    RegisTodo.place(x=59, y=535)

    #####################################################################################

    frameTabExcel = tk.Frame(
        mainWindow,
        bg="#8A8F87",
        width=650,
        height=600
    )
    frameTabExcel.place(x=118, y=107)

    rueda_y = tk.Scrollbar(frameTabExcel, orient="vertical")
    rueda_y.pack(side="left", fill="y")

    #Estilo de la tabla del excel

    Estilo = ttk.Style()
    Estilo.configure(
        "Treeview",
        background="#F7F4EC",
        fieldbackground="#F7F4EC",
        foreground="#2E322E"             
    )
    Estilo.configure(
        "Treeview.Heading",
        background="#1D7A6E",
        foreground="#2E322E",
        font=("Serif", 11, "bold")
    )

    Estilo.map(
        "Treeview.Heading",
        background=[("active", "#3FA66B")]
    )

    #####################################################################################

    tabla = ttk.Treeview(
        frameTabExcel,
        columns=("Fecha", "Producto", "Precio", "Cantidad", "Tipo"),
        show="headings",
        yscrollcommand=rueda_y.set,
        height=26,
    )
    tabla.pack(fill="both", expand=True)

    rueda_y.config(command=tabla.yview)

    tabla.heading("Fecha", text="Fecha")
    tabla.heading("Producto", text="Producto")
    tabla.heading("Precio", text="Precio")
    tabla.heading("Cantidad", text="Cantidad")
    tabla.heading("Tipo", text="Tipo")

    tabla.column("Fecha", width=110, anchor="center")
    tabla.column("Producto", width=220, anchor="center")
    tabla.column("Precio", width=106, anchor="center")
    tabla.column("Cantidad", width=75, anchor="center")
    tabla.column("Tipo", width=90, anchor="center")

    fc.cargar_tabla_transacciones(tabla, usrActual)

    frameExportExcel = tk.Frame(
        mainWindow, 
        bg="#8A8F87",
        width=616,
        height=77
    )
    frameExportExcel.place(x=118, y=673)

    botonExportExcel = tk.Button(
        frameExportExcel,
        text="Exportar Excel (.xlsx)",
        font=("Serif", 15, "bold"),
        bg="#00FF7F",
        fg="#2E322E",
        relief="flat",
        highlightthickness=2,
        highlightbackground="#2E322E",
        command=lambda: fc.exportar_reporte_en_excel(usrActual),
        activebackground="#2E322E",
        activeforeground="#00FF7F"
    )
    botonExportExcel.place(x=345, y=17)

    botonBorrExcel = tk.Button(
        frameExportExcel,
        text="Reiniciar Operaciones",
        font=("Serif", 15, "bold"),
        bg="#C0503B",
        fg="#2E322E",
        relief="flat",
        highlightthickness=2,
        highlightbackground="#2E322E",
        command=lambda: (os.system(f"rm Reporte-EasyFinance-{usrActual}.xlsx"), fc.cargar_tabla_transacciones(tabla, usrActual), fc.calcular_utilidades_totales(usrActual, varUtililidad, varUtililidadEgresos, varUtililidadEnvios, varUtililidadTotal, utilTotal)),
        activebackground="#2E322E",
        activeforeground="#C0503B"
    )
    botonBorrExcel.place(x=20, y=17)

def Mostrar_ventana_graficos(Usuario_actual):

    for widget in mainWindow.winfo_children():
        widget.destroy()

    Usr = Usuario_actual

    fecha_actual = fc.Obtener_fecha_actual()
    fecha_actual2 = date.today().strftime("%Y-%m-%d")
    
    imagen = Image.open("imagenes/_.png")
    imagen = imagen.resize((1500,800))
    imagen_fondo = ImageTk.PhotoImage(imagen)

    labelImg = tk.Label(mainWindow, image=imagen_fondo)
    labelImg.image = imagen_fondo
    labelImg.place(x=0, y=0)

    mainWindow.configure(bg="#F7F4EC")

    #####################################################################################

    frameMenu = tk.Frame(
        mainWindow,
        bg="#8FBC8F",
        width=100,
        height=800,
        highlightthickness=1,
        highlightbackground="#2E322E",
    )
    frameMenu.pack(
        fill="both", 
        expand=False,
        side="left"
    )

    # Boton de la Casa

    logoCasa = Image.open("imagenes/casa.png")
    logoCasa = logoCasa.resize((77, 77))
    logoCasaFond = ImageTk.PhotoImage(logoCasa)
    botonCasa = tk.Button(
        frameMenu,
        bg="#2E322E",
        image=logoCasaFond,
        relief="flat",
        command=lambda: Mostrar_ventana_principal(Usuario_actual),
    )
    botonCasa.image = logoCasaFond
    botonCasa.place(x=8, y=8)

    # Boton de los Graficos

    logoGraf = Image.open("imagenes/graficos.png")
    logoGraf = logoGraf.resize((77, 77))
    logoGraficoFond = ImageTk.PhotoImage(logoGraf)
    botonGraf = tk.Button(
        frameMenu,
        bg="#2E322E",
        image=logoGraficoFond,
        relief="flat",
        command=lambda: Mostrar_ventana_graficos(Usuario_actual),
    )
    botonGraf.image = logoGraficoFond
    botonGraf.place(x=8, y=98)

    # Boton del Logout

    logoLogout = Image.open("imagenes/logout.png")
    logoLogout = logoLogout.resize((77, 77))
    logoLogoutFond = ImageTk.PhotoImage(logoLogout)
    botonLogout = tk.Button(
        frameMenu,
        bg="#8FBC8F",
        image=logoLogoutFond,
        relief="flat",
        command=lambda: (fc.logout(varUtililidad, varUtililidadEgresos, varUtililidadEnvios, varUtililidadTotal), Mostrar_ventana_login()),
        highlightthickness=0,
        activebackground="#5E8A6E"
    )
    botonLogout.image = logoLogoutFond
    botonLogout.place(x=8, y=710)

    #####################################################################################

    figuraGraf = plt.figure(figsize=(16, 9), dpi=90)
    figuraGraf.patch.set_facecolor("#8FBC8F")
    figuraGraf.patch.set_alpha(1.0)
    varsGraf = figuraGraf.add_subplot(111)

    # Graficaa

    resultdo = fc.calcular_Punto_Equilibrio(Usuario_actual)

    if resultdo is None:
        varsGraf.text(
            0.5, 0.5,
            "No hay suficientes datos para calcular el punto de equilibrio.",
            ha="center", va="center", fontsize=14, color="#2E322E",
            transform=varsGraf.transAxes
        )
    elif resultdo["Alcanzable"] == False:
        varsGraf.text(
            0.5, 0.5,
            "El precio de venta no cubre el costo variable.\nNo existe punto de equilibrio alcanzable.",
            ha="center", va="center", fontsize=14, color="#C0503B",
            transform=varsGraf.transAxes
        )
    else:
        P = resultdo["P"]
        CV = resultdo["CV"]
        CF = resultdo["CF"]
        xEq = resultdo["X"]
        ingresoEq = resultdo["Ingreso"]

        x_max = xEq * 2 if xEq > 0 else 10
        x = np.linspace(0, x_max, 100)
        ingreso = P * x
        costo = CF + CV * x

        varsGraf.plot(x, ingreso, label="Ingreso Total I(x)", color="#3FA66B", linewidth=2.5)
        varsGraf.plot(x, costo, label="Costo Total C(x)", color="#C0503B", linewidth=2.5)
        varsGraf.scatter([xEq], [ingresoEq], color="#1D7A6E", s=100, zorder=5, label="Punto de Equilibrio")

        varsGraf.annotate(
            f"x = {xEq:.1f} unidades\n$ {ingresoEq:.2f}",
            xy=(xEq, ingresoEq),
            xytext=(xEq + x_max * 0.05, ingresoEq),
            fontsize=11,
            color="#2E322E"
        )

        varsGraf.set_facecolor("#F7F4EC")
        varsGraf.set_xlabel("Unidades vendidas", fontsize=12, color="#2E322E")
        varsGraf.set_ylabel("Dinero", fontsize=12, color="#2E322E")
        varsGraf.set_title(f"Punto de Equilibrio - {Usuario_actual}", fontsize=15, fontweight="bold", color="#2E322E")
        varsGraf.legend(loc="upper left", fontsize=10)
        varsGraf.grid(True, linestyle="--", alpha=0.4)

    ####################################################################################################################

    grafCanvas = FigureCanvasTkAgg(
        figuraGraf,
        master=mainWindow
    )
    grafCanvas.get_tk_widget().place(x=100, y=-20)

    grafCanvas.draw()

    barHeramientas = NavigationToolbar2Tk(grafCanvas, mainWindow)
    barHeramientas.update()

Mostrar_ventana_login()
mainWindow.mainloop()