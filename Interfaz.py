import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import func as fc

##############################################################################
##############################################################################

def login_interfaz(user, passwd):

    Usuario = user.get()
    Contraseña = passwd.get()
    Sesion = (f"{Usuario},{Contraseña}")

    Usuario_formateado = ""
    Letra1 = Usuario[0].upper()
    Resto = Usuario[1:]
    Usuario_formateado = Letra1 + Resto

    with open("base_de_datos.txt", "r") as f:
        lectura = f.read()
    if Sesion in lectura :
        print("Bienvenido al systema")
        Mostrar_ventana_principal(Usuario_formateado)
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

def Mostrar_ventana_login():

    for widget in Main_window.winfo_children():
        widget.destroy()
    

    frame_login = tk.Frame(
        Main_window,
        bg="#FAF0E6",
        width=1000,
        height=800,
    )
    frame_login.pack(

        fill="both", 
        expand=False,
        side="left"
    )

    imagen = Image.open("imagenes/imagen_login.jpg")
    imagen = imagen.resize((1000,800))
    imagen_login = ImageTk.PhotoImage(imagen)

    label_imagen = tk.Label(frame_login, image=imagen_login)
    label_imagen.image = imagen_login
    label_imagen.pack(pady=0)

    Bienvenido = tk.Label(
        frame_login,
        text=" Bienvenido a EasyFinance ",
        font=("Serif", 30, "bold"),
        bg="Black",
        fg="White"
    ).place(x=250, y=20)


    Frame_botones = tk.Frame(
        Main_window,
        bg="#8FBC8F",
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
        text="Inicio de Sesión",
        font=("Serif", 23, "bold"),
        bg="#8FBC8F",
        fg="White"
    )
    Inicio_sesion.pack(pady=50, padx=127)


    Texto_Sesion = tk.Label(
        Frame_botones,
        text="Ingrese su nombre de usuario:",
        font=("Serif", 15, "bold"),
        bg="#8FBC8F",
        fg="Black"
    )
    Texto_Sesion.place(y=200, x=15)

    Ingreso__sesion = tk.Entry(
        Frame_botones,
        width=40,
        font=("Serif", 15, "bold"),
        bg="#DCDCDC",
        fg="Black"
    )
    Ingreso__sesion.place(y=240, x=15)

    Texto_Sesion = tk.Label(
        Frame_botones,
        text="Ingrese su contraseña:",
        font=("Serif", 15, "bold"),
        bg="#8FBC8F",
        fg="Black"
    )
    Texto_Sesion.place(y=280, x=15)

    Ingreso__passwd = tk.Entry(
        Frame_botones,
        show="#",
        width=40,
        font=("Serif", 15, "bold"),
        bg="#DCDCDC",
        fg="Black"
    )
    Ingreso__passwd.place(y=320, x=15)


    Boton_ingresar = tk.Button(
        Frame_botones,
        text="Ingresar",
        font=("Serif", 15, "bold"),
        bg="#DCDCDC",
        fg="Black",
        command=lambda:login_interfaz(Ingreso__sesion, Ingreso__passwd)
    )
    Boton_ingresar.place(y=380, x=180)

    Logo = Image.open("imagenes/logo.png")
    Logo = Logo.resize((400, 200))
    Final_Logo = ImageTk.PhotoImage(Logo)

    Label_logo = tk.Label(
        Frame_botones,
        image=Final_Logo,
        bg="#8FBC8F"
    )
    Label_logo.image = Final_Logo
    Label_logo.place(y=440, x=50)

    No_tiene_cuenta = tk.Button(
        Frame_botones,
        text="  ¿No tiene cuenta?. Regístrese aquí  ",
        font=("Serif", 12, "bold"),
        bg="#8FBC8F",
        fg="Black",
        highlightthickness=1,
        highlightbackground="#F0F8FF",
        command=Mostrar_ventana_registro

    )
    No_tiene_cuenta.place(y=750, x=100)


def Mostrar_ventana_registro():
    for widget in Main_window.winfo_children():
            widget.destroy()
        
    
    frame_login = tk.Frame(
        Main_window,
        bg="#FAF0E6",
        width=1000,
        height=800,
    )
    frame_login.pack(

        fill="both", 
        expand=False,
        side="left"
    )

    imagen = Image.open("imagenes/imagen_login.jpg")
    imagen = imagen.resize((1000,800))
    imagen_login = ImageTk.PhotoImage(imagen)

    label_imagen = tk.Label(frame_login, image=imagen_login)
    label_imagen.image = imagen_login
    label_imagen.pack(pady=0)

    Bienvenido = tk.Label(
        frame_login,
        text=" Bienvenido a EasyFinance ",
        font=("Serif", 30, "bold"),
        bg="Black",
        fg="White"
    ).place(x=250, y=20)


    Frame_botones = tk.Frame(
        Main_window,
        bg="",
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
        bg="#8FBC8F",
        fg="White"
    )
    Inicio_sesion.place(y=50, x=100)


    Texto_Sesion = tk.Label(
        Frame_botones,
        text="Ingrese su nuevo usuario:",
        font=("Serif", 15, "bold"),
        bg="#8FBC8F",
        fg="Black"
    )
    Texto_Sesion.place(y=200, x=15)

    Ingreso__sesion = tk.Entry(
        Frame_botones,
        width=40,
        font=("Serif", 15, "bold"),
        bg="#DCDCDC",
        fg="Black"
    )
    Ingreso__sesion.place(y=240, x=15)


    Texto_Sesion = tk.Label(
        Frame_botones,
        text="Cree una contraseña segura:",
        font=("Serif", 15, "bold"),
        bg="#8FBC8F",
        fg="Black"
    )
    Texto_Sesion.place(y=280, x=15)

    Ingreso__passwd = tk.Entry(
        Frame_botones,
        show="#",
        width=40,
        font=("Serif", 15, "bold"),
        bg="#DCDCDC",
        fg="Black"
    )
    Ingreso__passwd.place(y=320, x=15)

    Boton_ingresar = tk.Button(
        Frame_botones,
        text="Registrarme",
        font=("Serif", 15, "bold"),
        bg="#DCDCDC",
        fg="Black",
        command=lambda: fc.registro_interfaz(Ingreso__sesion, Ingreso__passwd)
    )
    Boton_ingresar.place(y=380, x=170)

    Logo = Image.open("imagenes/logo.png")
    Logo = Logo.resize((400, 200))
    Final_Logo = ImageTk.PhotoImage(Logo)

    Label_logo = tk.Label(
        Frame_botones,
        image=Final_Logo,
        bg="#8FBC8F"
    )
    Label_logo.image = Final_Logo
    Label_logo.place(y=440, x=50)

    No_tiene_cuenta = tk.Button(
        Frame_botones,
        text="  ¿Ya tiene cuenta?. Inicie sesión aquí  ",
        font=("Serif", 12, "bold"),
        bg="#8FBC8F",
        fg="Black",
        highlightthickness=1,
        highlightbackground="#F0F8FF",
        command=Mostrar_ventana_login
    )
    No_tiene_cuenta.place(y=750, x=90)

def Mostrar_ventana_principal(Usuario_actual):
    for widget in Main_window.winfo_children():
        widget.destroy()

    fecha_actual = fc.Obtener_fecha_actual()

    Main_window.configure(bg="#FFFFFF")

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

    tk.Label(
        Main_window,
        text=f"¡Bienvenido a EasyFinance!, {Usuario_actual}",
        bg="#FFFFFF",
        fg="#000000",
        font=("Serif", 20, "bold")
    ).place(x=135, y=15)

    tk.Label(
        Main_window,
        text=f"Asi va tu tienda hoy, {fecha_actual}",
        bg="#FFFFFF",
        fg="#808080",
        font=("Serif", 15, "bold")
    ).place(x=135, y=60)

    frame_utilidad = tk.Frame(
        Main_window,
        bg="#8FBC8F",
        width=700,
        height=100
    )
    frame_utilidad.place(x=750, y=30)

    frame_registrar_operacion = tk.Frame(
        Main_window,
        bg="#8FBC8F",
        width=700,
        height=600
    )
    frame_registrar_operacion.place(x=750, y=150)

    frame_tipo_operacion = tk.Frame(
        frame_registrar_operacion,
        bg="#F0F8FF",
        width=700,
        height=100
    )
    frame_tipo_operacion.place(x=750, y=770)

    registrar_ingreso = tk.Button(
        frame_tipo_operacion,
        text="Registrar Ingreso",
        font=("Serif", 15, "bold"),
        bg="#DCDCDC",
        fg="Black"
    )
    registrar_ingreso.place(x=10, y=10)

    registrar_egreso = tk.Button(
        frame_tipo_operacion,
        text="Registrar Egreso",
        font=("Serif", 15, "bold"),
        bg="#DCDCDC",
        fg="Black"
    )
    registrar_egreso.place(x=10, y=60)

    registrar_envio = tk.Button(
        frame_tipo_operacion,
        text="Registrar Envío",
        font=("Serif", 15, "bold"),
        bg="#DCDCDC",
        fg="Black"
    )
    registrar_envio.place(x=10, y=110)

Mostrar_ventana_login()
Main_window.mainloop()