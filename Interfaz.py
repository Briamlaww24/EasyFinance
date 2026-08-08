import os
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
import func as fc
from datetime import date

##############################################################################
##############################################################################

def login_interfaz(user, passwd, recuerdame):

    Usuario = user.get()
    Contraseña = passwd.get()
    Sesion = (f"{Usuario},{Contraseña}")

    Usuario_formateado = ""
    Letra1 = Usuario[0].upper()
    Resto = Usuario[1:]
    Usuario_formateado = Letra1 + Resto

    with open("base_de_datos.txt", "r", encoding="utf-8") as f:
        lectura = f.read()

    if Sesion in lectura :
        print("Bienvenido al systema")
        Mostrar_ventana_principal(Usuario_formateado)

        if recuerdame.get():
            with open("recuerdame.txt", "w", encoding="utf-8") as f:
                f.write(Sesion)
        else:
            with open("recuerdame.txt", "w", encoding="utf-8") as f:
                f.write("")

    else:
        print("Error")
        tk.messagebox.showerror("Error", "Usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.")

################################################################################
################################################################################

Main_window = tk.Tk()
Main_window.title("EasyFinance")
Main_window.geometry("1500x800")
Main_window.resizable(False, False)
Main_window.configure(bg="#8FBC8F")

recuerdame = tk.BooleanVar(value=False)

def Mostrar_ventana_login():

    if os.path.exists("recuerdame.txt"):
        with open("recuerdame.txt", "r", encoding="utf-8") as f:
            usuario_guardado = f.read().strip()

        if usuario_guardado:
            with open("base_de_datos.txt", "r", encoding="utf-8") as f:
                lectura = f.read()

            if usuario_guardado in lectura:
                usuario_sesion = usuario_guardado.split(",")[0]
                usuario_sesion = usuario_sesion[:1].upper() + usuario_sesion[1:]
                Mostrar_ventana_principal(usuario_sesion)
                return

    for widget in Main_window.winfo_children():
        widget.destroy()
    

    frame_login = tk.Frame(
        Main_window,
        bg="#F7F4EC",
        width=1000,
        height=800,
        borderwidth=0,
        highlightthickness=0
    )
    frame_login.pack(

        fill="both", 
        expand=False,
        side="left"
    )

    imagen = Image.open("imagenes/login_ilustracion.png")
    imagen = imagen.resize((1000,800))
    imagen_login = ImageTk.PhotoImage(imagen)

    label_imagen = tk.Label(frame_login, image=imagen_login)
    label_imagen.image = imagen_login
    label_imagen.pack(pady=0)

    Frame_botones = tk.Frame(
        Main_window,
        bg="#80ac8e",
        width=500,
        height=800,
        borderwidth=0,
        highlightthickness=0
    )
    Frame_botones.pack(
        fill="both",
        expand=False,
        side="right"
    )

    Inicio_sesion = tk.Label(
        Frame_botones,
        text="Inicio de Sesión",
        font=("Serif", 23, "bold"),
        bg="#80ac8e",
        fg="White"
    )
    Inicio_sesion.pack(pady=50, padx=127)


    Texto_Sesion = tk.Label(
        Frame_botones,
        text="Ingrese su nombre de usuario:",
        font=("Serif", 15, "bold"),
        bg="#80ac8e",
        fg="#2E322E"
    )
    Texto_Sesion.place(y=200, x=15)

    Ingreso__sesion = tk.Entry(
        Frame_botones,
        width=40,
        font=("Serif", 15, "bold"),
        bg="#F7F4EC",
        fg="#2E322E",
        relief="solid"
    )
    Ingreso__sesion.place(y=240, x=15)

    Texto_Sesion = tk.Label(
        Frame_botones,
        text="Ingrese su contraseña:",
        font=("Serif", 15, "bold"),
        bg="#80ac8e",
        fg="#2E322E",
    )
    Texto_Sesion.place(y=280, x=15)

    Ingreso__passwd = tk.Entry(
        Frame_botones,
        show="#",
        width=40,
        font=("Serif", 15, "bold"),
        bg="#F7F4EC",
        fg="#2E322E",
        relief="solid"
    )
    Ingreso__passwd.place(y=320, x=15)

    

    tk.Checkbutton(
        Frame_botones,
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

  

    Boton_ingresar = tk.Button(
        Frame_botones,
        text="Ingresar",
        font=("Serif", 15, "bold"),
        bg="#F7F4EC",
        fg="#2E322E",
        command=lambda:login_interfaz(Ingreso__sesion, Ingreso__passwd, recuerdame),
        relief="raised",
    )
    Boton_ingresar.place(y=380, x=180)

    Logo = Image.open("imagenes/logo.png")
    Logo = Logo.resize((400, 188))
    Final_Logo = ImageTk.PhotoImage(Logo)

    Label_logo = tk.Label(
        Frame_botones,
        image=Final_Logo,
        bg="#80ac8e"
    )
    Label_logo.image = Final_Logo
    Label_logo.place(y=440, x=50)

    Logo2 = Image.open("imagenes/logo.png")
    Logo2 = Logo.resize((200, 94))
    Final_Logo2 = ImageTk.PhotoImage(Logo2)

    Label_logo2 = tk.Label(
        frame_login,
        image=Final_Logo2,
        bg="#92b89e"
    )
    Label_logo2.image =Final_Logo2
    Label_logo2.place(x=2, y=2)

    No_tiene_cuenta = tk.Button(
        Frame_botones,
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
    for widget in Main_window.winfo_children():
            widget.destroy()   
    
    frame_login = tk.Frame(
        Main_window,
        bg="#F7F4EC",
        width=1000,
        height=800,
    )
    frame_login.pack(

        fill="both", 
        expand=False,
        side="left"
    )

    imagen = Image.open("imagenes/login_ilustracion.png")
    imagen = imagen.resize((1000,800))
    imagen_login = ImageTk.PhotoImage(imagen)

    label_imagen = tk.Label(frame_login, image=imagen_login)
    label_imagen.image = imagen_login
    label_imagen.pack(pady=0)

    Frame_botones = tk.Frame(
        Main_window,
        bg="#80ac8e",
        width=500,
        height=800
    )
    Frame_botones.pack(
        fill="both",
        expand=False,
        side="right"
    )

    Inicio_sesion = tk.Label(
        Frame_botones,
        text="Registro de Usuario",
        font=("Serif", 23, "bold"),
        bg="#80ac8e",
        fg="White"
    )
    Inicio_sesion.place(y=50, x=100)


    Texto_Sesion = tk.Label(
        Frame_botones,
        text="Ingrese su nuevo usuario:",
        font=("Serif", 15, "bold"),
        bg="#80ac8e",
        fg="#2E322E"
    )
    Texto_Sesion.place(y=200, x=15)

    Ingreso__sesion = tk.Entry(
        Frame_botones,
        width=40,
        font=("Serif", 15, "bold"),
        bg="#F7F4EC",
        fg="#2E322E",
        relief="solid"
    )
    Ingreso__sesion.place(y=240, x=15)


    Texto_Sesion = tk.Label(
        Frame_botones,
        text="Cree una contraseña segura:",
        font=("Serif", 15, "bold"),
        bg="#80ac8e",
        fg="#2E322E"
    )
    Texto_Sesion.place(y=280, x=15)

    Ingreso__passwd = tk.Entry(
        Frame_botones,
        show="#",
        width=40,
        font=("Serif", 15, "bold"),
        bg="#F7F4EC",
        fg="#2E322E",
        relief="solid"
    )
    Ingreso__passwd.place(y=320, x=15)

    Boton_ingresar = tk.Button(
        Frame_botones,
        text="Registrarme",
        font=("Serif", 15, "bold"),
        bg="#F7F4EC",
        fg="#2E322E",
        command=lambda: fc.registro_interfaz(Ingreso__sesion, Ingreso__passwd)
    )
    Boton_ingresar.place(y=380, x=170)

    Logo = Image.open("imagenes/logo.png")
    Logo = Logo.resize((400, 200))
    Final_Logo = ImageTk.PhotoImage(Logo)

    Label_logo = tk.Label(
        Frame_botones,
        image=Final_Logo,
        bg="#80ac8e"
    )
    Label_logo.image = Final_Logo
    Label_logo.place(y=440, x=50)

    No_tiene_cuenta = tk.Button(
        Frame_botones,
        text="  ¿Ya tiene cuenta?. Inicie sesión aquí  ",
        font=("Serif", 12, "bold"),
        bg="#80ac8e",
        fg="#2E322E",
        highlightthickness=1,
        highlightbackground="#2E322E",
        command=Mostrar_ventana_login,
        relief="flat",
    )
    No_tiene_cuenta.place(y=750, x=90)

var_utililidad_total = tk.DoubleVar(value=0.0)
var_utililidad_envios = tk.DoubleVar(value=0.0)
var_utililidad_egresos = tk.DoubleVar(value=0.0)
var_utililidad = tk.DoubleVar(value=0.0)

def Mostrar_ventana_principal(Usuario_actual):
    for widget in Main_window.winfo_children():
        widget.destroy()

    User = Usuario_actual

    fecha_actual = fc.Obtener_fecha_actual()
    fecha_actual2 = date.today().strftime("%Y-%m-%d")
    
    imagen = Image.open("imagenes/_.png")
    imagen = imagen.resize((1500,800))
    imagen_fondo = ImageTk.PhotoImage(imagen)

    label_imagen = tk.Label(Main_window, image=imagen_fondo)
    label_imagen.image = imagen_fondo
    label_imagen.place(x=0, y=0)

    Main_window.configure(bg="#F7F4EC")

    ###########################################################################################

    frame_menu = tk.Frame(
        Main_window,
        bg="#8FBC8F",
        width=100,
        height=800,
    )
    frame_menu.pack(
        fill="both", 
        expand=False,
        side="left"
    )

    # Boton de la Casa

    logo_casa = Image.open("imagenes/casa.png")
    logo_casa = logo_casa.resize((77, 77))
    logo_casa_fondo = ImageTk.PhotoImage(logo_casa)
    Boton_casa = tk.Button(
        frame_menu,
        bg="#2E322E",
        image=logo_casa_fondo,
        relief="flat",
        command=lambda: Mostrar_ventana_principal(Usuario_actual),
    )
    Boton_casa.image = logo_casa_fondo
    Boton_casa.place(x=8, y=8)

    # Boton de los Graficos

    logo_grafico = Image.open("imagenes/graficos.png")
    logo_grafico = logo_grafico.resize((77, 77))
    logo_grafico_fondo = ImageTk.PhotoImage(logo_grafico)
    Boton_grafico = tk.Button(
        frame_menu,
        bg="#2E322E",
        image=logo_grafico_fondo,
        relief="flat",
        command=lambda: Mostrar_ventana_graficos(Usuario_actual),
    )
    Boton_grafico.image = logo_grafico_fondo
    Boton_grafico.place(x=8, y=98)

    # Boton del Logout

    logo_logout = Image.open("imagenes/logout.png")
    logo_logout = logo_logout.resize((77, 77))
    logo_logout_fondo = ImageTk.PhotoImage(logo_logout)
    Boton_logout = tk.Button(
        frame_menu,
        bg="#8FBC8F",
        image=logo_logout_fondo,
        relief="flat",
        command=lambda: (fc.logout(var_utililidad, var_utililidad_egresos, var_utililidad_envios, var_utililidad_total), Mostrar_ventana_login()),
        highlightthickness=0,
        activebackground="#5E8A6E"
    )
    Boton_logout.image = logo_logout_fondo
    Boton_logout.place(x=8, y=710)


    ###########################################################################################

    tk.Label(
        Main_window,
        text=f"¡Bienvenido a EasyFinance!, {Usuario_actual}",
        bg="#F7F4EC",
        fg="#2E322E",
        font=("Serif", 20, "bold")
    ).place(x=135, y=15)

    tk.Label(
        Main_window,
        text=f"Asi va tu tienda hoy, {fecha_actual}",
        bg="#F7F4EC",
        fg="#8A8F87",
        font=("Serif", 15, "bold")
    ).place(x=135, y=60)

 #######################################################
 # Frame de la Utilidad

    frame_utilidad = tk.Frame(
        Main_window,
        bg="#8FBC8F",
        width=730,
        height=100
    )
    frame_utilidad.place(x=755, y=30)

    numeros_utilidad = tk.Frame(
        frame_utilidad,
        bg="#F7F4EC",
        width=170,
        height=80,
    )
    numeros_utilidad.place(x=10, y=10)

    tk.Label(
        numeros_utilidad,
        text="INGRESOS:",
        font=("Serif", 10, "bold"),
        fg="#8A8F87",
        bg="#F7F4EC"
    ).place(x=5, y=5)

    Utilidad_ingresos = tk.Label(
        numeros_utilidad,
        textvariable=var_utililidad,
        font=("Serif", 20, "bold"),
        fg="#3FA66B",
        bg="#F7F4EC"
    )
    Utilidad_ingresos.place(x=5, y=30)

    # Framde de los egresos

    numeros_utilidad_egresos = tk.Frame(
        frame_utilidad,
        bg="#F7F4EC",
        width=170,
        height=80,
    )
    numeros_utilidad_egresos.place(x=190, y=10)

    tk.Label(
        numeros_utilidad_egresos,
        text="EGRESOS:",
        font=("Serif", 10, "bold"),
        fg="#8A8F87",
        bg="#F7F4EC"
    ).place(x=5, y=5)

    Utilidad_egresos = tk.Label(
        numeros_utilidad_egresos,
        textvariable=var_utililidad_egresos,
        font=("Serif", 20, "bold"),
        fg="#C0503B",
        bg="#F7F4EC"
    )
    Utilidad_egresos.place(x=5, y=30)

    # Frame de los Envios

    numeros_utilidad_envios = tk.Frame(
        frame_utilidad,
        bg="#F7F4EC",
        width=170,
        height=80,
    )
    numeros_utilidad_envios.place(x=370, y=10)

    tk.Label(
        numeros_utilidad_envios,
        text="ENVÍOS:",
        font=("Serif", 10, "bold"),
        fg="#8A8F87",
        bg="#F7F4EC"
    ).place(x=5, y=5)

    Utilidad_envios = tk.Label(
        numeros_utilidad_envios,
        textvariable=var_utililidad_envios,
        font=("Serif", 20, "bold"),
        fg="#C98A2E",
        bg="#F7F4EC"
    )
    Utilidad_envios.place(x=5, y=30)

    # Frame de la Utilidad Total

    numeros_utilidad_total = tk.Frame(
        frame_utilidad,
        bg="#2E322E",
        width=170,
        height=80,
    )
    numeros_utilidad_total.place(x=550, y=10)

    tk.Label(
        numeros_utilidad_total,
        text="UTILIDAD NETA:",
        font=("Serif", 10, "bold"),
        fg="#8A8F87",
        bg="#2E322E"
    ).place(x=5, y=5)

    Utilidad_total = tk.Label(
        numeros_utilidad_total,
        textvariable=var_utililidad_total,
        font=("Serif", 20, "bold"),
        fg="#3FA66B",
        bg="#2E322E"
    )
    Utilidad_total.place(x=5, y=30)

    fc.calcular_utilidades_totales(Usuario_actual, var_utililidad, var_utililidad_egresos, var_utililidad_envios, var_utililidad_total, Utilidad_total)

 #########################################################

    frame_registrar_operacion = tk.Frame(
        Main_window,
        bg="#8FBC8F",
        width=730,
        height=600
    )
    frame_registrar_operacion.place(x=755, y=150)

    tk.Label(
        frame_registrar_operacion,
        text="Llene los campos para registrar una operación:",
        font=("Serif", 15, "bold"),
        bg="#8FBC8F",
        fg="#2E322E"
    ).place(x=30, y=7)

    frame_tipo_operacion = tk.Frame(
        frame_registrar_operacion,
        bg="#F7F4EC",
        width=614,
        height=60
    )
    frame_tipo_operacion.place(x=59, y=60)

    tipo_operacion = tk.StringVar()

    registrar_ingreso = tk.Button(
        frame_tipo_operacion,
        text="Registrar Ingreso",
        font=("Serif", 15, "bold"),
        bg="#1D7A6E",
        fg="Black",
        activebackground="#3FA66B",
        relief="flat",
        highlightthickness=2,
        highlightbackground="#2E322E",
        command=lambda: setear_variable_tipo_operacion(tipo_operacion, "+(Ingreso)"),
    )
    registrar_ingreso.place(x=10, y=10)

    registrar_egreso = tk.Button(
        frame_tipo_operacion,
        text="Registrar Egreso",
        font=("Serif", 15, "bold"),
        bg="#1D7A6E",
        fg="Black",
        activebackground="#3FA66B",
        relief="flat",
        highlightthickness=2,
        highlightbackground="#2E322E",
        command=lambda: setear_variable_tipo_operacion(tipo_operacion, "-(Egreso)")
    )
    registrar_egreso.place(x=220, y=10)

    registrar_envio = tk.Button(
        frame_tipo_operacion,
        text="Registrar Envío",
        font=("Serif", 15, "bold"),
        bg="#1D7A6E",
        fg="Black",
        activebackground="#3FA66B",
        relief="flat",
        highlightthickness=2,
        highlightbackground="#2E322E",
        command=lambda: setear_variable_tipo_operacion(tipo_operacion, "-(Envio)")
    )
    registrar_envio.place(x=420, y=10)

    def setear_variable_tipo_operacion(operacion, tipo):
            operacion.set(tipo)
            fc.definir_color_botones_ingreso(tipo_operacion, registrar_ingreso, registrar_egreso, registrar_envio)
    

    tk.Label(
        frame_registrar_operacion,
        text="Pequeña Descripción: ",
        font=("Serif", 15, "bold"),
        bg="#8FBC8F",
        fg="#2E322E"
    ).place(x=59, y=140)

    Descripcion = tk.Entry(
        frame_registrar_operacion,
        width=55,
        font=("Serif", 15, "bold"),
        bg="#F7F4EC",
        fg="#2E322E",
        relief="solid",
        highlightcolor="#0e7c66",
        highlightthickness=2,
    )
    Descripcion.place(x=59, y=180)

    tk.Label(
        frame_registrar_operacion,
        text="Monto: ",
        font=("Serif", 15, "bold"),
        bg="#8FBC8F",
        fg="#2E322E"
    ).place(x=59, y=230)

    Monto = tk.Entry(
        frame_registrar_operacion,
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
        frame_registrar_operacion,
        text="Cantidad: ",
        font=("Serif", 15, "bold"),
        bg="#8FBC8F",
        fg="#2E322E"
    ).place(x=500, y=230)

    Cantidad = tk.Entry(
        frame_registrar_operacion,
        width=15,
        font=("Serif", 15, "bold"),
        bg="#F7F4EC",
        fg="#2E322E",
        relief="solid",
        highlightcolor="#0e7c66",
        highlightthickness=2
    )
    Cantidad.place(x=500, y=270)

    tk.Label(
        frame_registrar_operacion,
        text="______________________________________________________________________",
        font=("Serif", 15, "bold"),
        bg="#8FBC8F",
        fg="#2E322E"
    ).place(x=50, y=330)

    tk.Label(
        frame_registrar_operacion,
        text=f"Nota: La operacion se registrara con la fecha actual. \n ({fecha_actual})",
        font=("Serif", 15, "bold"),
        bg="#8FBC8F",
        fg="#2E322E",
    ).place(x=100, y="377")
    fc.actualizar_hora(frame_registrar_operacion, fecha_actual)

    Registrar_todo = tk.Button(
        frame_registrar_operacion,
        text="REGISTRAR",
        font=("Serif", 15, "bold"),
        width=54,
        bg="#00FF7F",
        fg="Black",
        activebackground="#C0503B",
        relief="flat",
        highlightthickness=2,
        highlightbackground="#2E322E",
        command=lambda: (fc.registrar_operacion_interfaz(fecha_actual2, tipo_operacion, Descripcion, Monto, Cantidad, User, var_utililidad, var_utililidad_egresos, var_utililidad_envios, var_utililidad_total, Utilidad_total), fc.cargar_tabla_transacciones(tabla, Usuario_actual))
    )
    Registrar_todo.place(x=59, y=535)

    ##############################################################################
    ##############################################################################

    frame_tabla_excel = tk.Frame(
        Main_window,
        bg="#8A8F87",
        width=650,
        height=600
    )
    frame_tabla_excel.place(x=118, y=107)

    rueda_y = tk.Scrollbar(frame_tabla_excel, orient="vertical")
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

    ########################################################

    tabla = ttk.Treeview(
        frame_tabla_excel,
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

    fc.cargar_tabla_transacciones(tabla, Usuario_actual)

    frame_exportar_excel = tk.Frame(
        Main_window, 
        bg="#8A8F87",
        width=616,
        height=77
    )
    frame_exportar_excel.place(x=118, y=673)

    Boton_exportar_excel = tk.Button(
        frame_exportar_excel,
        text="Exportar Excel (.xlsx)",
        font=("Serif", 15, "bold"),
        bg="#00FF7F",
        fg="#2E322E",
        relief="flat",
        highlightthickness=2,
        highlightbackground="#2E322E",
        command=lambda: os.system(f"xdg-open Reporte-EasyFinance-{Usuario_actual}.xlsx")
    )
    Boton_exportar_excel.place(x=345, y=17)

    Boton_borrar_excel = tk.Button(
        frame_exportar_excel,
        text="Reiniciar Operaciones",
        font=("Serif", 15, "bold"),
        bg="#C0503B",
        fg="#2E322E",
        relief="flat",
        highlightthickness=2,
        highlightbackground="#2E322E",
        command=lambda: (os.system(f"rm Reporte-EasyFinance-{Usuario_actual}.xlsx"), fc.cargar_tabla_transacciones(tabla, Usuario_actual), fc.calcular_utilidades_totales(Usuario_actual, var_utililidad, var_utililidad_egresos, var_utililidad_envios, var_utililidad_total, Utilidad_total))
    )


def Mostrar_ventana_graficos(Usuario_actual):

    for widget in Main_window.winfo_children():
        widget.destroy()

    User = Usuario_actual

    fecha_actual = fc.Obtener_fecha_actual()
    fecha_actual2 = date.today().strftime("%Y-%m-%d")
    
    imagen = Image.open("imagenes/_.png")
    imagen = imagen.resize((1500,800))
    imagen_fondo = ImageTk.PhotoImage(imagen)

    label_imagen = tk.Label(Main_window, image=imagen_fondo)
    label_imagen.image = imagen_fondo
    label_imagen.place(x=0, y=0)

    Main_window.configure(bg="#F7F4EC")

    ###########################################################################################

    frame_menu = tk.Frame(
        Main_window,
        bg="#8FBC8F",
        width=100,
        height=800,
    )
    frame_menu.pack(
        fill="both", 
        expand=False,
        side="left"
    )

    # Boton de la Casa

    logo_casa = Image.open("imagenes/casa.png")
    logo_casa = logo_casa.resize((77, 77))
    logo_casa_fondo = ImageTk.PhotoImage(logo_casa)
    Boton_casa = tk.Button(
        frame_menu,
        bg="#2E322E",
        image=logo_casa_fondo,
        relief="flat",
        command=lambda: Mostrar_ventana_principal(Usuario_actual),
    )
    Boton_casa.image = logo_casa_fondo
    Boton_casa.place(x=8, y=8)

    # Boton de los Graficos

    logo_grafico = Image.open("imagenes/graficos.png")
    logo_grafico = logo_grafico.resize((77, 77))
    logo_grafico_fondo = ImageTk.PhotoImage(logo_grafico)
    Boton_grafico = tk.Button(
        frame_menu,
        bg="#2E322E",
        image=logo_grafico_fondo,
        relief="flat",
        command=lambda: Mostrar_ventana_graficos(Usuario_actual),
    )
    Boton_grafico.image = logo_grafico_fondo
    Boton_grafico.place(x=8, y=98)

    # Boton del Logout

    logo_logout = Image.open("imagenes/logout.png")
    logo_logout = logo_logout.resize((77, 77))
    logo_logout_fondo = ImageTk.PhotoImage(logo_logout)
    Boton_logout = tk.Button(
        frame_menu,
        bg="#8FBC8F",
        image=logo_logout_fondo,
        relief="flat",
        command=lambda: (fc.logout(), Mostrar_ventana_login()),
        highlightthickness=0,
        activebackground="#5E8A6E"
    )
    Boton_logout.image = logo_logout_fondo
    Boton_logout.place(x=8, y=710)

    ################################################################################




Mostrar_ventana_login()
Main_window.mainloop()