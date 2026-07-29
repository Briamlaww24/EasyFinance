import questionary
import random
import os
import time

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