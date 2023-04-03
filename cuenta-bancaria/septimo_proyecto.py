from random import *

#DECLARANDO CLASE "PERSONA"


class persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

#CREANDO OBJETO DE LA CLASE PERSONA


class cliente(persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = int(balance)

    def __str__(self):
        return f"{self.nombre} {self.apellido}\nSu numero de cuenta es {self.numero_cuenta} y su saldo es ${self.balance}"

    def depositar(self,monto_deposito):
        self.balance += monto_deposito
        print("***Deposito aceptado***")

    def retirar(self,monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("***Retiro realizado***")
        else:
            print("***Fondos insuficientes***")

#FUNCION PARA CREAR CLIENTE


def crear_cliente():
    nombre_cl = input("Ingrese su nombre: ")
    apellido_cl = input("Ingrese su apellido: ")
    numero_cuenta = randint(0000,9999)
    cliente1 = cliente(nombre_cl,apellido_cl,numero_cuenta)
    return cliente1

#CREANDO INICIO DEL PROGRAMA


def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != "3":
        print("""Elije las siguientes opciones:
        [1] - Depositar
        [2] - Retirar
        [3] - Salir""")
        opcion = input()

        if opcion == "1":
            monto_dep = int(input("Monto a depositar: "))
            mi_cliente.depositar(monto_dep)
        elif opcion == "2":
            monto_ret = int(input("Monto a retirar: "))
            mi_cliente.retirar(monto_ret)
        print(mi_cliente)
    print("Gracias por operar con nosotros.")

#EJECUCION


inicio()

