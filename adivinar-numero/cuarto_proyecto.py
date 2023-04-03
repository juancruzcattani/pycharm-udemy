#libreria para generar numero al azar

from random import *

numero_usuario = 0
#generador de numero al azar
numero_azar = randint(1, 100)
intentos = 0
nombre_usuario = input("Ingrese su nombre de usuario: ")
print("\n")
print(f"Hola {nombre_usuario} a continuacion el programa eligira un numero al azar del 1 al 100\nUsted deberá adivinarlo en 8 intentos.")
print("\n")

while intentos < 8:
    numero_usuario = int(input("Ingrese un numero del 1 al 100: "))
    # vidas
    intentos += 1
    if numero_usuario not in range(1,100):
        print("Debes ingresar un numero del 1 al 100.")
    elif numero_usuario > numero_azar:
        print("El numero que ingresaste es mayor a mi numero, vuelve a intentarlo")
    elif numero_usuario < numero_azar:
        print("El numero que ingresaste es menor a mi numero, vuelve a intentarlo")
    else:
        print(f"Felicitaciones {nombre_usuario}, me has ganado en {intentos} intentos ")
        break

if numero_usuario != numero_azar:
    print(f"Lo siento, se teh han agotado los intentos, el numero secreto era {numero_azar}")