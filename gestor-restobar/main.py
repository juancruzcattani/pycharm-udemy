from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox


operador = ""
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 2.99]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 3.10]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14]

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ""
    visor_calculadora.delete(0, END)


def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ""

#Funcion que configura los checkboxs y sus cantidades
def revisar_check():
    x = 0
    for c in cuadro_comida:
        if variables_comida[x].get() == 1:
            cuadro_comida[x].config(state=NORMAL)
            if cuadro_comida[x].get() == "0":
                cuadro_comida[x].delete(0, END)
            cuadro_comida[x].focus()
        else:
            cuadro_comida[x].config(state=DISABLED)
            texto_comida[x].set("0")
        x += 1

    x = 0
    for c in cuadro_bebidas:
        if variables_bebidas[x].get() == 1:
            cuadro_bebidas[x].config(state=NORMAL)
            if cuadro_bebidas[x].get() == "0":
                cuadro_bebidas[x].delete(0, END)
            cuadro_bebidas[x].focus()
        else:
            cuadro_bebidas[x].config(state=DISABLED)
            texto_bebidas[x].set("0")
        x += 1

    x = 0
    for c in cuadro_postres:
        if variables_postres[x].get() == 1:
            cuadro_postres[x].config(state=NORMAL)
            if cuadro_postres[x].get() == "0":
                cuadro_postres[x].delete(0, END)
            cuadro_postres[x].focus()
        else:
            cuadro_postres[x].config(state=DISABLED)
            texto_postres[x].set("0")
        x += 1

#Funcino que calcula el total
def total():
    subtotal_comidas = 0
    p = 0
    for cantidad in texto_comida:
        subtotal_comidas = subtotal_comidas + (float(cantidad.get()) * precios_comida[p])
        p += 1

    subtotal_bebidas = 0
    p = 0
    for cantidad in texto_bebidas:
        subtotal_bebidas = subtotal_bebidas + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    subtotal_postres = 0
    p = 0
    for cantidad in texto_postres:
        subtotal_postres = subtotal_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1

    subtotal = subtotal_comidas + subtotal_bebidas + subtotal_postres
    impuestos = subtotal * 0.07
    total = subtotal + impuestos

    var_costo_comida.set(f"$ {round(subtotal_comidas, 2)}")
    var_costo_bebida.set(f"$ {round(subtotal_bebidas, 2)}")
    var_costo_postres.set(f"$ {round(subtotal_postres, 2)}")
    var_subtotal.set(f"$ {round(subtotal, 2)}")
    var_impuestos.set(f"$ {round(impuestos, 2)}")
    var_total.set(f"$ {round(total, 2)}")

#Funcion recibo
def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f"N# - {random.randint(1000, 9999)}"
    fecha = datetime.datetime.now()
    fecha_recibo = f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}"
    texto_recibo.insert(END, f"Datos:\t{num_recibo}\t\t\t{fecha_recibo}\n")
    texto_recibo.insert(END, f"*" * 70 + "\n")
    texto_recibo.insert(END, f"Items\t\tCantidad\t\tCosto Items\n")
    texto_recibo.insert(END, f"-" * 83 + "\n")

    x = 0
    for comida in texto_comida:
        if comida.get() != "0":
            texto_recibo.insert(END, f"{lista_comidas[x]}\t\t{comida.get()}\t\t${int(comida.get()) * precios_comida[x]}\n")

        x += 1

    x = 0
    for bebida in texto_bebidas:
        if bebida.get() != "0":
            texto_recibo.insert(END, f"{lista_bebidas[x]}\t\t{bebida.get()}\t\t${int(bebida.get()) * precios_bebida[x]}\n")

        x += 1

    x = 0
    for postres in texto_postres:
        if postres.get() != "0":
            texto_recibo.insert(END, f"{lista_postres[x]}\t\t{postres.get()}\t\t${int(postres.get()) * precios_postres[x]}\n")

        x += 1

    texto_recibo.insert(END, f"-" * 83 + "\n")
    texto_recibo.insert(END, f"Costo de la comida:\t\t\t\t{var_costo_comida.get()}\n")
    texto_recibo.insert(END, f"Costo de la bebidas:\t\t\t\t{var_costo_bebida.get()}\n")
    texto_recibo.insert(END, f"Costo de la postres:\t\t\t\t{var_costo_postres.get()}\n")
    texto_recibo.insert(END, f"-" * 83 + "\n")
    texto_recibo.insert(END, f"Subtotal:\t\t\t\t{var_subtotal.get()}\n")
    texto_recibo.insert(END, f"Impuestos:\t\t\t\t{var_impuestos.get()}\n")
    texto_recibo.insert(END, f"Total:\t\t\t\t{var_total.get()}\n")
    texto_recibo.insert(END, f"*" * 70 + "\n")
    texto_recibo.insert(END, "\tLo esperamos pronto!")

#Guardar recibo
def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo("Informacion", "Su recibo ha sido guardado")

def resetear():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set("0")

    for texto in texto_bebidas:
        texto.set("0")

    for texto in texto_postres:
        texto.set("0")

    for cuadro in cuadro_comida:
        cuadro.config(state=DISABLED)

    for cuadro in cuadro_bebidas:
        cuadro.config(state=DISABLED)

    for cuadro in cuadro_postres:
        cuadro.config(state=DISABLED)

    for var in variables_comida:
        var.set(0)

    for var in variables_bebidas:
        var.set(0)

    for var in variables_postres:
        var.set(0)

    var_costo_comida.set("")
    var_costo_bebida.set("")
    var_costo_postres.set("")
    var_subtotal.set("")
    var_impuestos.set("")
    var_total.set("")

# iniciar tkinter
aplicacion = Tk()

# tamaño de la aplicacion
aplicacion.geometry("1160x560+100+100")

# evitar maximizacion de la pantalla
aplicacion.resizable(False, False)

# titulo aplicacion
aplicacion.title("RESTOBAR - SISTEMA DE GESTION")

# color fondo
aplicacion.config(bg="gray80")

# panel superior
panel_superior = Frame(aplicacion,
                       bd=1,
                       relief=FLAT)
panel_superior.pack(side=TOP)

# etiqueta titulo
etiqueta_titulo = Label(panel_superior,
                        text="SISTEMA DE GESTION",
                        fg="gray20",
                        font=("Dosis", 50),
                        bg="gray80",
                        width=20)
etiqueta_titulo.grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion,
                        bd=1,
                        relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# panel de costos
panel_costos = Frame(panel_izquierdo,
                     bd=1,
                     relief=FLAT,
                     bg="azure4",
                     padx=85,
                     pady=85)
panel_costos.pack(side=BOTTOM)

# panel de comidas
panel_comidas = LabelFrame(panel_izquierdo,
                           text="COMIDAS",
                           font=("Dosis", 14, "bold"),
                           bd=1,
                           relief=FLAT,
                           fg="gray20"
                           )
panel_comidas.pack(side=LEFT)

# panel de bebidas
panel_bebidas = LabelFrame(panel_izquierdo,
                           text="BEBIDAS",
                           font=("Dosis", 14, "bold"),
                           bd=1,
                           relief=FLAT,
                           fg="gray20")
panel_bebidas.pack(side=LEFT)

# panel de postres
panel_postres = LabelFrame(panel_izquierdo,
                           text="POSTRES",
                           font=("Dosis", 14, "bold"),
                           bd=1,
                           relief=FLAT,
                           fg="gray20")
panel_postres.pack(side=LEFT)

# PANEL DE LA DERECHA
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame(panel_derecha,
                          bd=1,
                          relief=FLAT,
                          bg="gray80")
panel_calculadora.pack()

# panel recibo
panel_recibo = Frame(panel_derecha,
                     bd=1,
                     relief=FLAT,
                     bg="gray80")
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_derecha,
                      bd=1,
                      relief=FLAT,
                      bg="gray80")
panel_botones.pack()

# listas de productos
lista_comidas = ["Suprema", "Fideos", "Ravioles", "Pizza Especial", "Pizza Muzarella", "Papas Fritas"]
lista_postres = ["Helado", "Frutillas c/c", "Brownie", "Brownie c/h", "Ensd.frut", "Tiramisu"]
lista_bebidas = ["Agua", "Cerveza", "Vino", "Cocacola", "Sprite", "Fanta"]

# generar items comida
variables_comida = []
cuadro_comida = []
texto_comida = []
contador = 0

for comida in lista_comidas:
    # crear checkbutton
    variables_comida.append("")
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=("Dosis", 12, "bold"),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W)

    # cuadros de entrada
    cuadro_comida.append("")
    texto_comida.append("")
    texto_comida[contador] = StringVar()
    texto_comida[contador].set("0")
    cuadro_comida[contador] = Entry(panel_comidas,
                                    font=("Dosis", 12, "bold"),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_comida[contador])
    cuadro_comida[contador].grid(row=contador,
                                 column=1,
                                 padx=20)

    contador += 1

# generar items bebidas
variables_bebidas = []
cuadro_bebidas = []
texto_bebidas = []
contador = 0

for bebidas in lista_bebidas:
    variables_bebidas.append("")
    variables_bebidas[contador] = IntVar()
    bebidas = Checkbutton(panel_bebidas,
                          text=bebidas.title(),
                          font=("Dosis", 12, "bold"),
                          onvalue=1,
                          offvalue=0,
                          variable=variables_bebidas[contador],
                          command=revisar_check)
    bebidas.grid(row=contador,
                 column=0,
                 sticky=W)

    # cuadros de entrada
    cuadro_bebidas.append("")
    texto_bebidas.append("")
    texto_bebidas[contador] = StringVar()
    texto_bebidas[contador].set("0")
    cuadro_bebidas[contador] = Entry(panel_bebidas,
                                     font=("Dosis", 12, "bold"),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebidas[contador])
    cuadro_bebidas[contador].grid(row=contador,
                                  column=1,
                                  padx=20)

    contador += 1

# generar items postres
variables_postres = []
cuadro_postres = []
texto_postres = []
contador = 0

for postres in lista_postres:
    variables_postres.append("")
    variables_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres,
                          text=postres.title(),
                          font=("Dosis", 12, "bold"),
                          onvalue=1,
                          offvalue=0,
                          variable=variables_postres[contador],
                          command=revisar_check)
    postres.grid(row=contador,
                 column=0,
                 sticky=W)

    # cuadros de entrada
    cuadro_postres.append("")
    texto_postres.append("")
    texto_postres[contador] = StringVar()
    texto_postres[contador].set("0")
    cuadro_postres[contador] = Entry(panel_postres,
                                     font=("Dosis", 12, "bold"),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postres[contador])
    cuadro_postres[contador].grid(row=contador,
                                  column=1,
                                  padx=20)

    contador += 1

#etiquetas de costos y campos de entrada
#variables
var_costo_comida = StringVar()
var_costo_postres = StringVar()
var_costo_bebida = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()

etiqueta_costo_comida = Label(panel_costos,
                              text="Costo comida",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white",
                              )
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_costo_comida)

texto_costo_comida.grid(row=0, column=1, padx=41)

#bebidas
etiqueta_costo_bebida = Label(panel_costos,
                              text="Costo bebida",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white",
                              )
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_costo_bebida)

texto_costo_bebida.grid(row=1, column=1, padx=41)

#postres
etiqueta_costo_postres = Label(panel_costos,
                              text="Costo postres",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white",)
etiqueta_costo_postres.grid(row=2, column=0)


#subtotal
texto_subtotal = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_subtotal)

texto_subtotal.grid(row=2, column=1, padx=41)

etiqueta_subtotal = Label(panel_costos,
                              text="Subtotal",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white",)
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_subtotal)

texto_subtotal.grid(row=0, column=3, padx=41)

#impuestos
texto_impuestos = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_impuestos)

texto_impuestos.grid(row=2, column=1, padx=41)

etiqueta_impuestos = Label(panel_costos,
                              text="Impuestos",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white",)
etiqueta_impuestos.grid(row=1, column=2)

texto_impuestos = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_impuestos)

texto_impuestos.grid(row=1, column=3, padx=41)

#total
texto_total = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_total)

texto_total.grid(row=2, column=1, padx=41)

etiqueta_total = Label(panel_costos,
                              text="Total",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_total)

texto_total.grid(row=2, column=3, padx=41)

#botones
botones = ["total", "recibo", "guardar", "resetear"]
botones_creados = []

columnas = 0

for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=("Dosis", 12, "bold"),
                   fg="white",
                   bg="azure4",
                   bd=1,
                   width=10)

    botones_creados.append(boton)

    boton.grid(row=0,
               column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

#area recibo
texto_recibo = Text(panel_recibo,
                    font=("Dosis", 12, "bold"),
                    bd=3,
                    width=47,
                    height=12)
texto_recibo.grid(row=0,
                  column=0)

#calculadora

visor_calculadora = Entry(panel_calculadora,
                          font=("Dosis", 16, "bold"),
                          width=35,
                          bd=3)
visor_calculadora.grid(row=8, column=0, columnspan=4)

botones_calculadoras = ["7", "8", "9", "+",
                        "4", "5", "6", "-",
                        "1", "2", "3", "x",
                        "RES", "BORRAR", "0", "/"]
botones_guardados = []


fila = 0
columna = 0

for boton in botones_calculadoras:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=("Dosis", 14, "bold"),
                   fg="white",
                   bg="azure4",
                   bd=1,
                   width=8)

    botones_guardados.append(boton)

    boton.grid(row=fila,
               column=columna)
    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda : click_boton("7"))
botones_guardados[1].config(command=lambda : click_boton("8"))
botones_guardados[2].config(command=lambda : click_boton("9"))
botones_guardados[3].config(command=lambda : click_boton("+"))
botones_guardados[4].config(command=lambda : click_boton("4"))
botones_guardados[5].config(command=lambda : click_boton("5"))
botones_guardados[6].config(command=lambda : click_boton("6"))
botones_guardados[7].config(command=lambda : click_boton("-"))
botones_guardados[8].config(command=lambda : click_boton("1"))
botones_guardados[9].config(command=lambda : click_boton("2"))
botones_guardados[10].config(command=lambda : click_boton("3"))
botones_guardados[11].config(command=lambda : click_boton("*"))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton("0"))
botones_guardados[15].config(command=lambda : click_boton("/"))




# evitar que la pantalla se cierre
aplicacion.mainloop()
