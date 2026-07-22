"""
Control Financiero para una Tienda Online
Autor: Briam Leyva Arévalo
Descripción: Registra ingresos, egresos y envíos, calcula utilidad
             y genera un reporte mensual. Los datos se guardan en
             un archivo JSON para que persistan entre ejecuciones.
"""

import json
import os
from datetime import datetime

ARCHIVO_DATOS = "movimientos.json"


# ------------------------------------------------------------------
# 1. CARGA Y GUARDADO DE DATOS
# ------------------------------------------------------------------
def cargar_datos():
    """Lee el archivo JSON si existe; si no, devuelve lista vacía."""
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def guardar_datos(movimientos):
    """Escribe la lista de movimientos en el archivo JSON."""
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
        json.dump(movimientos, f, ensure_ascii=False, indent=4)


# ------------------------------------------------------------------
# 2. VALIDACIÓN DE ENTRADAS
# ------------------------------------------------------------------
def pedir_monto(mensaje):
    """Pide un número positivo hasta que el usuario lo ingrese bien."""
    while True:
        try:
            monto = float(input(mensaje))
            if monto <= 0:
                print("El monto debe ser mayor a cero.")
                continue
            return monto
        except ValueError:
            print("Ingresa un número válido (ej: 25.50).")


def pedir_fecha():
    """Permite usar la fecha actual o ingresar una manualmente."""
    resp = input("¿Usar fecha de hoy? (s/n): ").strip().lower()
    if resp == "s":
        return datetime.now().strftime("%Y-%m-%d")
    while True:
        fecha = input("Ingresa la fecha (YYYY-MM-DD): ")
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            return fecha
        except ValueError:
            print("Formato inválido. Ejemplo correcto: 2026-07-16")


# ------------------------------------------------------------------
# 3. REGISTRO DE MOVIMIENTOS
# ------------------------------------------------------------------
def registrar_movimiento(movimientos, tipo):
    """
    tipo puede ser: 'ingreso', 'egreso' o 'envio'.
    Todos comparten la misma estructura, solo cambia la categoría.
    """
    print(f"\n--- Registrar {tipo} ---")
    descripcion = input("Descripción: ").strip()
    monto = pedir_monto("Monto: $")
    fecha = pedir_fecha()

    nuevo = {
        "fecha": fecha,
        "tipo": tipo,
        "descripcion": descripcion,
        "monto": monto,
    }
    movimientos.append(nuevo)
    guardar_datos(movimientos)
    print(f"{tipo.capitalize()} registrado correctamente.\n")


# ------------------------------------------------------------------
# 4. CÁLCULO DE UTILIDAD
# ------------------------------------------------------------------
def calcular_utilidad(movimientos, filtrados=None):
    """
    Utilidad = ingresos - (egresos + envios)
    Si se pasa 'filtrados', calcula solo sobre ese subconjunto
    (usado para el reporte mensual).
    """
    datos = filtrados if filtrados is not None else movimientos

    total_ingresos = sum(m["monto"] for m in datos if m["tipo"] == "ingreso")
    total_egresos = sum(m["monto"] for m in datos if m["tipo"] == "egreso")
    total_envios = sum(m["monto"] for m in datos if m["tipo"] == "envio")
    utilidad = total_ingresos - total_egresos - total_envios

    return total_ingresos, total_egresos, total_envios, utilidad


def mostrar_utilidad_total(movimientos):
    if not movimientos:
        print("\nNo hay movimientos registrados todavía.\n")
        return
    ingresos, egresos, envios, utilidad = calcular_utilidad(movimientos)
    print("\n--- Utilidad total acumulada ---")
    print(f"Ingresos totales: ${ingresos:.2f}")
    print(f"Egresos totales:  ${egresos:.2f}")
    print(f"Envíos totales:   ${envios:.2f}")
    print(f"Utilidad neta:    ${utilidad:.2f}\n")


# ------------------------------------------------------------------
# 5. REPORTE MENSUAL
# ------------------------------------------------------------------
def reporte_mensual(movimientos):
    if not movimientos:
        print("\nNo hay movimientos registrados todavía.\n")
        return

    anio = input("Año a consultar (YYYY): ").strip()
    mes = input("Mes a consultar (MM): ").strip().zfill(2)
    prefijo = f"{anio}-{mes}"

    filtrados = [m for m in movimientos if m["fecha"].startswith(prefijo)]

    if not filtrados:
        print(f"\nNo hay movimientos para {prefijo}.\n")
        return

    ingresos, egresos, envios, utilidad = calcular_utilidad(movimientos, filtrados)

    print(f"\n===== Reporte de {prefijo} =====")
    print(f"{'Fecha':<12}{'Tipo':<12}{'Descripción':<25}{'Monto':>10}")
    print("-" * 60)
    for m in sorted(filtrados, key=lambda x: x["fecha"]):
        print(f"{m['fecha']:<12}{m['tipo']:<12}{m['descripcion']:<25}{m['monto']:>10.2f}")
    print("-" * 60)
    print(f"Ingresos: ${ingresos:.2f}")
    print(f"Egresos:  ${egresos:.2f}")
    print(f"Envíos:   ${envios:.2f}")
    print(f"Utilidad: ${utilidad:.2f}")

    guardar = input("\n¿Guardar este reporte en un archivo .txt? (s/n): ").strip().lower()
    if guardar == "s":
        nombre_archivo = f"reporte_{prefijo}.txt"
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write(f"Reporte de {prefijo}\n")
            f.write(f"{'Fecha':<12}{'Tipo':<12}{'Descripción':<25}{'Monto':>10}\n")
            f.write("-" * 60 + "\n")
            for m in sorted(filtrados, key=lambda x: x["fecha"]):
                f.write(f"{m['fecha']:<12}{m['tipo']:<12}{m['descripcion']:<25}{m['monto']:>10.2f}\n")
            f.write("-" * 60 + "\n")
            f.write(f"Ingresos: ${ingresos:.2f}\n")
            f.write(f"Egresos:  ${egresos:.2f}\n")
            f.write(f"Envíos:   ${envios:.2f}\n")
            f.write(f"Utilidad: ${utilidad:.2f}\n")
        print(f"Reporte guardado como '{nombre_archivo}'.\n")


# ------------------------------------------------------------------
# 6. MENÚ PRINCIPAL
# ------------------------------------------------------------------
def mostrar_menu():
    print("=" * 40)
    print("   CONTROL FINANCIERO - TIENDA ONLINE")
    print("=" * 40)
    print("1. Registrar ingreso")
    print("2. Registrar egreso")
    print("3. Registrar envío")
    print("4. Ver utilidad total")
    print("5. Reporte mensual")
    print("6. Salir")


def main():
    movimientos = cargar_datos()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            registrar_movimiento(movimientos, "ingreso")
        elif opcion == "2":
            registrar_movimiento(movimientos, "egreso")
        elif opcion == "3":
            registrar_movimiento(movimientos, "envio")
        elif opcion == "4":
            mostrar_utilidad_total(movimientos)
        elif opcion == "5":
            reporte_mensual(movimientos)
        elif opcion == "6":
            print("\n¡Hasta luego!")
            break
        else:
            print("\nOpción no válida, intenta de nuevo.\n")


if __name__ == "__main__":
    main()
