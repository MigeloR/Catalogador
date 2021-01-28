"""Objetivo: crear documentos sql"""

import os


# tablas = ['tipos',]
# esto es de prueba
tablas = ['tipos', 'acciones', 'seguidores', 'entrenadores']
t_tipos = ['id', 'nombre']
dic_tablas = {
    'tipos': t_tipos,
}



def tuplas(e):
    """llena las tuplas"""
    numero = 1
    print("Elige la columna a llenar: ")
    d_tablas = dic_tablas[e]
    # print(d_tablas)
    values = []
    for i in d_tablas:
        print(f"{numero}) {i}")
        numero += 1
    try:
        eleccion = int(input()) - 1
        a = d_tablas[eleccion]
        print(f"Has elegido {a}")
        d = input("ingresa el dato: ")
        values.append(d)
    except IndexError:
        run()        
    return values


def tabla():
    elegir = print("elige una tabla: ")
    numero = 1
    for i in tablas:
        print(f"{numero}) {tablas[numero-1]}")
        numero += 1


def run():
    tabla()
    try:
        eleccion = int(input()) - 1
        e = tablas[eleccion]
        print(f"Has elegido {e}")
    except IndexError:
        run()
    # de aquí debería seguir el llenado de columnas, tupla por tuplas:
    z = tuplas(e)
    print(f"""
    
    {z}
    
    
    """)
    # lo que viene en adelante creará un documento en sql para exportar:
    file = open("/pkmn_datos.sql", "w")
    # file.write("Primera línea" + os.linesep)
    # file.write("Segunda línea")
    file.write(f"""INSERT INTO `tipos`(nombre)
    VALUES {z}
    ;")""")
    file.close()


if '__main__' == __name__:
    run()
    # tabla()