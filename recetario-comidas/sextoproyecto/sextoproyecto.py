from os import system
from pathlib import Path
import os

#DECLARANDO MI RUTA

mi_ruta = Path(Path.home(), "Desktop", "Pycharm-Udemy", "recetario-comidas", "sextoproyecto", "Recetas")


#PIDIENDO NOMBRE AL USUARIO


nombre = input("Ingrese su nombre de usuario: ")

#CONTADOR DE RECETAS


def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1

    return contador

#INICIO DEL PROGRAMA

def inicio():

    system("cls")
    print("*" * 50)
    print(f"Bienvenido {nombre} al adminsitrador de recetas")
    print("*" * 50)
    print("\n")
    print(f"Las recetas se encuentran en:\n{mi_ruta}\nScon en total {contar_recetas(mi_ruta)} recetas")

    eleccion_menu = "x"
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):

        print(f"{nombre} elige una opcion:")

        print("""
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoria nueva
        [4] - Eliminar receta
        [5] - Eliminar categoria
        [6] - Salir del programa""""")
        eleccion_menu = input()
    return int(eleccion_menu)

#FUNCION PARA MOSTRAR CATEGORIAS EN EL MENU


def mostrar_categoria(ruta):
    print("Categorias: ")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1
    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador +=1
    return lista_categorias

#FUNCION PARA ELEGIR LA CATEGORIA EN EL MENU


def elegir_categoria(lista):
    eleccion_correcta = "x"

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\nElije una categoria: ")

    return lista[int(eleccion_correcta) - 1]

#FUNCION PARA MOSTRAR LA RECETA EN EL MENU


def mostrar_recetas(ruta):
    print("Recetas: ")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob("*.txt"):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas

#FUNCION PARA ELEGIR RECETA UNA VEZ MOSTRADAS


def elegir_receta(lista):
    eleccion_receta = 'x'

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input("\nElije una receta: ")

    return lista[int(eleccion_receta) - 1]

#FUNCION PARA LEER RECETA


def leer_receta(receta):
    print(Path.read_text(receta))

#FUNCION PARA CREAR RECETA NUEVA


def crear_receta(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + ".txt"
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta,nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva,contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa receta ya existe")

#FUNCION PARA CREAR CATEGORIA


def crear_categoria(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de la nueva categoria: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta,nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu categoria, {nombre_categoria}, ha sido creada")
            existe = True
        else:
            print("Lo siento, esa categoria ya existe")

#FUNCION PARA ELIMINAR RECETA


def eliminar_receta(receta):
    Path.unlink(receta)
    print(f"La receta {receta.name} ha sido eliminada correctamente.")

#FUNCION PARA ELIMINAR CATEGORIA


def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"La categoria {categoria.name} ha sido eliminada correctamente.")

#FUNCION PARA VOLVER AL INICIO


def volver_inicio():
    eleccion_regresar = "x"

    while eleccion_regresar.lower() != "v":
        eleccion_regresar = input("\nPresione la letra 'V' para volver al inicio: ")


finalizar_programa = False

#MENU

while not finalizar_programa:
    menu = inicio()

    if menu == 1:
        mis_categorias = mostrar_categoria(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("No hay recetas en esta categoria.")
        else:
            mi_receta = elegir_receta(mis_recetas)
            leer_receta(mi_receta)
        volver_inicio()
    elif menu == 2:
        mis_categorias = mostrar_categoria(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()
    elif menu == 3:
        crear_categoria(mi_ruta)
        volver_inicio()
    elif menu == 4:
        mis_categorias = mostrar_categoria(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_receta(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()
    elif menu == 5:
        mis_categorias = mostrar_categoria(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()
    elif menu == 6:
        finalizar_programa = True


