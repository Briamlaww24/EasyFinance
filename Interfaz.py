import tkinter as tk
from PIL import Image, ImageTk
import func as fc

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
        command=lambda: fc.login_interfaz(Ingreso__sesion, Ingreso__passwd)
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


Mostrar_ventana_login()
Main_window.mainloop()