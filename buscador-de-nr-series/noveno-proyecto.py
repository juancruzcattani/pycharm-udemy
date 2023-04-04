import os
from pathlib import Path
import re
import datetime
import time
import math

#DECLARANDO VARIABLES

#VARIABLE CALCULO DE INICIO DE PROCES (TIME)
inicio_tiempo = time.time()

#VARIABLE BASE LOCAL
base = Path.home()

#VARIABLE CON RUTA DONDE VOY A TRABAJAR
ruta = Path(base, "Desktop", "Pycharm-Udemy", "buscador-de-nr-series", "Mi_Gran_Directorio")

#VARIABLE CON PATRON DE RE
mi_patron = r'N\D{3}-\d{5}'

#VARIABLE PARA UTILIZAR MI HORA LOCAL
hoy = datetime.date.today()

#LISTAS VACIAS

nrs_series = []
lstarchivos = []

#FUNCION PARA BUSCAR LOS NUMEROS DE SERIES


def buscar_numero(archivo,patron):
    abrir_archivo = open(archivo, "r")
    leer_contendio = abrir_archivo.read()
    if re.search(patron,leer_contendio):
        return re.search(patron,leer_contendio)
    else:
        return ""

#FUNCION PARA RELLENAR LAS LISTAS VACIAS CON LOS NUMEROS DE SERIE Y NOMBRE DE ARCHIVOS


def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for arc in archivo:
           resultado = buscar_numero(Path(carpeta,arc),mi_patron)
           if resultado != "":
               nrs_series.append(resultado.group())
               lstarchivos.append(arc.title())

#INICIO


def inicio():
    indice = 0
    print("-" * 50)
    print(f"\t\tFecha de busqueda: {hoy.day}/{hoy.month}/{hoy.year} ")
    print("\n")
    print("\t  ARCHIVO\t\t\t\t\t\tNR.SERIE")
    print("\t" + "  -------" + "\t\t\t\t\t\t" + "-" * 8)
    for arc in lstarchivos:
        print(f"\t{arc}\t\t\t\t\t{nrs_series[indice]}")
        indice += 1
    print("\n")
    print(f"Hay en total {len(nrs_series)} numeros de serie.")
    fin_tiempo = time.time()
    duracion = fin_tiempo - inicio_tiempo
    print(f"El proceso de recoleccion de numeros de serie tuvo una duracion de: {math.ceil(duracion)} segundos.")
    print("-" * 50)


crear_listas()
inicio()