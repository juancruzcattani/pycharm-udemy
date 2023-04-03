import random

# Lista de palabras posibles


palabras = ['manzana', 'banana', 'naranja', 'limon', 'piña']

# Escoger una palabra al azar


palabra = random.choice(palabras)

# Crear una lista para guardar las letras adivinadas


adivinadas = []

# Inicializar el contador de intentos fallidos


intentos_fallidos = 0

# Mientras el usuario no haya adivinado todas las letras y no haya superado el número máximo de intentos
while len(adivinadas) < len(palabra) and intentos_fallidos < 6:
    #Mostrar la palabra a adivinar, mostrando las letras adivinadas y dejando un guión bajo para las letras por adivinar

    display = ""
    for letra in palabra:
        if letra in adivinadas:
            display += letra
        else:
            display += "_"
    print(display)

    # Pedir al usuario que ingrese una letra

    letra = input("Ingrese una letra: ").lower()

    # Si la letra ya ha sido adivinada antes, mostrar un mensaje y seguir con el ciclo

    if letra in adivinadas:
        print("Ya adivinaste esa letra antes.")
        continue

    # Si la letra está en la palabra, agregarla a la lista de letras adivinadas
    # Si no está en la palabra, aumentar el contador de intentos fallidos

    if letra in palabra:
        adivinadas.append(letra)
    else:
        intentos_fallidos += 1
        print(f"Letra incorrecta. Te quedan {6 - intentos_fallidos} intentos.")

# Si el usuario adivinó todas las letras, mostrar un mensaje de felicitación
# Si el usuario superó el número máximo de intentos, mostrar un mensaje de derrota

if len(adivinadas) == len(palabra):
    print(f"¡Felicidades, adivinaste la palabra {palabra}!")
else:
    print(f"Lo siento, perdiste. La palabra era {palabra}.")


