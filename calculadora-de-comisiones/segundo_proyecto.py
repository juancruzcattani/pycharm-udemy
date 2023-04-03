nombre = input("Cual es tu nombre? ")
ventas = input("Cuanto vendiste este mes? ")

calculo_de_comision = round((int(ventas)*13)/100,2)

print(f"Hola {nombre}, tu comision por ventas de este mes es: {calculo_de_comision}")