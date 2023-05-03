import bs4
import requests


#creando url sin numero de pagina
url_base = "http://books.toscrape.com/catalogue/page-{}.html"


#lista vacia de titulos con sus condiciones (4 o 5 estrellas)
titulos_condicionados = []


#iterando paginas

for pag in range(1, 51):

    # creando sopa para cada pagina
    url_pagina = url_base.format(pag)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")

    # seleccionando datos de los libros
    libros = sopa.select(".product_pod")

    for libro in libros:
        # chequeando que tengan 4 o 5 estrellas los libros
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:

            #guardando titulo en variable
            titulo_libro = libro.select("a")[1]["title"]

            #agregar libro a la lista vacia
            titulos_condicionados.append(titulo_libro)


# ver libros en consola

for titulo in titulos_condicionados:
    print(titulo)

print(f"En total son {len(titulos_condicionados)} libros")







