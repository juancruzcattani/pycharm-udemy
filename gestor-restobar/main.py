from tkinter import *

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
lista_comidas = ["suprema", "fideos", "ravioles", "pizza especial", "pizza muzarella", "papas fritas"]
lista_postres = ["helado", "frutillas c/c", "brownie", "brownie c/h", "Ensd.frut", "tiramisu"]
lista_bebidas = ["agua", "cerveza", "vino", "cocacola", "sprite", "fanta"]

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
                         variable=variables_comida[contador])
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
                          variable=variables_bebidas[contador])
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
                          variable=variables_postres[contador])
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
columnas = 0

for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=("Dosis", 12, "bold"),
                   fg="white",
                   bg="azure4",
                   bd=1,
                   width=10)
    boton.grid(row=0,
               column=columnas)
    columnas += 1

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
    boton.grid(row=fila,
               column=columna)
    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0


# evitar que la pantalla se cierre
aplicacion.mainloop()
