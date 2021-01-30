import os


"""Objetivo: crear documentos sql"""


# listas:
tablas = ['tipos', 'pkmn']
c_tipos = ['id', 't_nombres']
c_pkmn = ['id', 'p_nombres']
dic_tipos = {
    'tipos': c_tipos,
    'pkmn': c_pkmn,
}


# 1: elegir tabla:
# Para esto debes tener una lista de tablas
def paso_1():
    elegir = print("elige una tabla: ")
    numero = 1
    for i in tablas:
        print(f"{numero}) {tablas[numero-1]}")
        numero += 1
    t = tabla()
    



def tabla():
    try:
        eleccion = int(input()) - 1
        if eleccion < 0:
            print("""valor no permitido
            """)
            tabla()
        else:
            t = tablas[eleccion]
            print(f"Has elegido {t}")
            return t
    except IndexError:
        print("""valor no permitido
        """)
        tabla()
    except ValueError:
        print("""valor no permitido
        """)
        tabla()



# def valor_tabla_no():
#     """agrupa valores no permitidos para la función tabla()"""
    # print("""valor no permitido
    # """)
    # paso_1()

# 2: elegir columna:
# para esto, tener una lista de columnas de cada tabla
def paso_2(t):
    print(f"aqu'i va {t}")
    # columna()


# def columna():


def run():
    # paso_1()
    t = paso_1() 
    paso_2(t) 


if '__main__' == __name__:
    run()
    # tabla()