""""
MODULO DONDE CREAMOS FUNCIONES GENERADORAS PARA TURNOS DE SUPUESTA FARMACIA, DIVIENDO LA CATEGORIA COSMETICA, FARMACIA Y PERFUMERIA.
"""

#GENERADOR DE TURNOS PARA PERFUMERIA.


def generador_perfumeria():

    for n in range(1, 1000):
        yield f"P-{n}"

#GENERADOR DE TURNOS PARA PARTE DE FARMACIA


def generador_farmacia():
    for n in range(1, 1000):
        yield f"F-{n}"

#GENERADOR DE TURNOS PARA COSMETICA


def generador_cosmetica():
    for n in range(1, 1000):
        yield f"C-{n}"

#VARIABLES QUE ALOJAN A LOS NUMEROS DE LOS GENERADORES.


p = generador_perfumeria()


f = generador_farmacia()


c = generador_cosmetica()

#DECORADOR DEL TICKET.


def decorar_generador(rubro):

    print("\n" + "*" * 10)
    print("Su numero de turno es: ")
    if rubro == "P":
        print(next(p))
    elif rubro == "F":
        print(next(f))
    else:
        print(next(c))
    print("Aguarde y será atendido")
    print("*" * 10 + "\n")





