tupla = ("hola", "Adiós")
lista = []
a_lista = [1,2,"hola"]


def conv_tupla(lista,a_lista):
    lista = tuple(a_lista)
    return lista


def run():
    #este es el modelo
    # lo que sigue 'abre' un archivo, entre parentesis se ubica la direccion en donde se creara
    file = open("d:/00Eternidad/00Drive/Documentos vivos/Proyectos/Rentabilidad/Base de datos SQL/pkmn/textual_origen.sql", "w")
    # lo que sigue será la primera línea del archivo:
    file.write("textual ;)")
    # puedes añadir otra línea bajo la estructura "file.write()". Entre paréntesis debe ir el contenido de la línea:
    # lo que sigue indica que se cierra el archivo:
    file.close()


def from_tupla():
    #imprime desde una tupla
    # lo que sigue 'abre' un archivo, entre parentesis se ubica la direccion en donde se creara
    file = open("d:/00Eternidad/00Drive/Documentos vivos/Proyectos/Rentabilidad/Base de datos SQL/pkmn/textual_tupla.sql", "w")
    # lo que sigue será la primera línea del archivo:
    file.write(f'{tupla[:]}')
    # puedes añadir otra línea bajo la estructura "file.write()". Entre paréntesis debe ir el contenido de la línea:
    # lo que sigue indica que se cierra el archivo:
    file.close()


def from_lista(lista,a_lista):
    print(f'estamos dentro de la impresión de lista y aquí esta vale: {lista[:]}')
    #imprime desde una tupla
    # lo que sigue 'abre' un archivo, entre parentesis se ubica la direccion en donde se creara
    file = open("d:/00Eternidad/00Drive/Documentos vivos/Proyectos/Rentabilidad/Base de datos SQL/pkmn/textual_lista.sql", "w")
    # lo que sigue será la primera línea del archivo:
    file.write(f'{lista[:]}')
    # puedes añadir otra línea bajo la estructura "file.write()". Entre paréntesis debe ir el contenido de la línea:
    # lo que sigue indica que se cierra el archivo:
    file.close()


if __name__ == '__main__':
    run()
    from_tupla()
    conv_tupla(lista,a_lista)
    from_lista(lista,a_lista)