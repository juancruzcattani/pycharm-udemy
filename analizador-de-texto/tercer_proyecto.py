#crear un programa que le pida al usuario que ingrese un texto cualquiera
#luego que ingrese 3 letras a su eleccion
#en base a esas 3 letras el programa debe hacer lo siguiente:
#1.cuantas veces aparece cada una de las letras que ingreso
#2.decir al usuario cuantas palabras hay a lo largo de todo el texto
#3. cual es la primera letra del texto y la ultima
#4 como quedaria el texto si invirtieramos el orden de las palabras
#5 nos va a decir si la palabra python se encuentra dentro del texto

ing_texto = input("Ingrese un texto de su preferencia: ")
letra_1 = input("Ingrese la primer letra a analizar: ")
letra_2 = input("Ingrese la segunda letra a analizar: ")
letra_3 = input("Ingrese la tercera letra a analizar: ")

texto_minusculas = ing_texto.lower()

buscar_letra_1 = texto_minusculas.count(letra_1) #buscando cuantas veces se repite en el texto la letra ingresada por el usuario
buscar_letra_2 = texto_minusculas.count(letra_2) #buscando cuantas veces se repite en el texto la letra ingresada por el usuario
buscar_letra_3 = texto_minusculas.count(letra_3)#buscando cuantas veces se repite en el texto la letra ingresada por el usuario
convirtiendo_a_lista = list(texto_minusculas.split())#convirtiendo a lista un string (el split se utiliza para tomar las palabras mediante los espacios)
cantidad_palabras_texto = len(convirtiendo_a_lista) #pidiendo la cantidad de palabras del texto(primero hacerlo lista)
primer_letra = texto_minusculas[0] #accediendo al primer indice del texto ingresado
ultima_letra = texto_minusculas[-1] #accediendo al ultimo indice del texto ingresado
convirtiendo_a_lista.reverse() #texto al revez
texto_invertido = " ".join(convirtiendo_a_lista)
python = "python" in texto_minusculas


print(f"La letra {letra_1} se repite {buscar_letra_1} veces en el texto")
print(f"La letra {letra_2} se repite {buscar_letra_2} veces en el texto")
print(f"La letra {letra_3} se repite {buscar_letra_3} veces en el texto")
print(f"El texto contiene {cantidad_palabras_texto} palabras")
print(f"El primer caracter del texto que ingresaste es {primer_letra}")
print(f"El ultimo caracter del texto que ingresaste es {ultima_letra}")
print(f"Tu texto dado vuelta sería así: {texto_invertido} ")
print("A continuacion, si la palabra Python figura en el texto que ingresaste, el programa devolvera True, sino False.")
print(python)

