from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side

def formatear_excel():
    Excel = load_workbook("Reporte-EasyFinance.xlsx")
    hoja = Excel["Datos"]

    color_fondo = PatternFill(
        fill_type="solid",
        fgColor="81c9fa"
    )   

    for celda in hoja[1]:
        celda.font = Font(bold=True, color="FFFFFF")
        celda.fill = color_fondo
        celda.alignment = Alignment(horizontal="center")

    Excel.save("Reporte-EasyFinance.xlsx")