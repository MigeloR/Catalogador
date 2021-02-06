d_op_240 = {
    '1': '$a Título uniforme (NR)',
    '2': '$d Fecha de la firma de un tratado (R)',
    '3': '$f Fecha de la obra (NR)',
    '4': '$g Información miscelánea (R)',
    '5': '$k Subencabezamiento de forma (R)',
    '6': '$l Lengua de la obra (NR)',
    '7': '$m Medio de interpretación (R)',
    '8': '$n Número de parte o sección de la obra (R)',
    '9': '$o Arreglo (NR)',
    '10': '$p Nombre de parte o sección de la obra (R)',
    '11': '$r Tonalidad (NR)',
    '12': '$s Versión (R)',
    '13': '$6 Enlace (NR)',
}


d_co_240_subcampos = {
    '$a Título uniforme (NR)': "",
    '$d Fecha de la firma de un tratado (R)': "",
    '$f Fecha de la obra (NR)': "",
    '$g Información miscelánea (R)': "",
    '$k Subencabezamiento de forma (R)': "",
    '$l Lengua de la obra (NR)': "",
    '$m Medio de interpretación (R)': "",
    '$n Número de parte o sección de la obra (R)': "",
    '$o Arreglo (NR)': "",
    '$p Nombre de parte o sección de la obra (R)': "",
    '$r Tonalidad (NR)': "",
    '$s Versión (R)': "",
    '$6 Enlace (NR)': "",
}


d_op_245 = {
    '1': '$a Título (NR)',
    '2': '$c Mención de responsabilidad, etc. (NR)',
    '3': '$f Fechas extremas (NR)',
    '4': '$g Fechas predominantes (NR)',
    '5': '$k Forma (R)',
    '6': '$n Número de parte o sección de la obra (R)',
    '7': '$p Nombre de parte o sección de la obra (R)',
    '8': '$s Versión (NR)',
    '9': '$6 Enlace (NR)',
}


d_co_245_subcampos = {
    '$a Título (NR)': "",
    '$c Mención de responsabilidad, etc. (NR)': "",
    '$f Fechas extremas (NR)': "",
    '$g Fechas predominantes (NR)': "",
    '$k Forma (R)': "",
    '$n Número de parte o sección de la obra (R)': "",
    '$p Nombre de parte o sección de la obra (R)': "",
    '$s Versión (NR)': "",
    '$6 Enlace (NR)': "",    
}


d_op_tablas = {
    '1': "240_Titulo_uniforme",
    '2': "245_Mencion_de_titulo",
}


d_co_tablas = {
    '240_Titulo_uniforme': d_co_240_subcampos,
    '245_Mencion_de_titulo': d_co_245_subcampos,
}


d_e_dop_XXX = {
    '1': 'd_op_240',
    '2': 'd_op_245',
}


de_dop_XXX = {
    'd_op_240': d_op_240,
    'd_op_245': d_op_245,
}


def tabla_elegida(eddddd):
    """aqui se eligen subcampos"""
    n = 1
    print("""
    campos actuales:
    """)
    for i in eddddd.values():
        print(f"{n}) {i}")
        n += 1
    sc = int(input("elige un subcampo: "))
    esc = eddddd[f'{sc}']
    print(esc)

    
def run():
    n = 1
    for i in d_op_tablas.values():
        print(f"{n}) {i}")
        n += 1
    e_d_co_tablas = int(input("""
    elige uno de los campos: """))
    edco = d_op_tablas[f'{e_d_co_tablas}']
    edco_sc = d_e_dop_XXX[f'{e_d_co_tablas}']
    print(f"sobre edco: {edco_sc} y {type(edco_sc)}")
    eddddd = de_dop_XXX[edco_sc]
    print(f"sobre eddddd: {eddddd} y {type(eddddd)}")
    tabla_elegida(eddddd)


if __name__ == '__main__':
    run()
    input()


# def f_co_columnas(ds):
#     """Aqui se editan los contenidos de las columnas (las columnas son los subcamos)"""
#     print("estado actual:")
#     n = 1
#     for i in d_co_tablas[ds].values():
#         # print(d_op_240[f'{n}'])
#         print(f"{d_op_240[f'{n}']}: {i}")
#         n += 1
#     print("")
#     d_co_240_subcampos[f'{ds}'] = input(f"escribe un valor para {ds}: ")
#     print("")
#     # con esto volvemos a elegir otra columna o la misma, si deseamos corregir:
#     f_se_columnas()


# def f_se_columnas(llave):
#     """Aqui se escogera un valor y este determinara la columna (las columnas son los subcamos) a editar"""
#     print("campos actuales:")
#     n = 1
#     print("0) salir") 
#     for i in d_co_240_subcampos.keys():
#         print(f"{n}) {i}")
#         n += 1
#     llave = int(input("Elige una campo a editar: "))
#     if llave == 0:
#         pass
#     else:
#         ds = d_op_240[f'{llave}']
#         print(ds)
#         d = d_co_240_subcampos[f'{ds}']
#         print(d)
#         # print("""
#         # a continuacion, optimizador
#         # """)
#         f_co_columnas(ds)
#     print("""
#     ya salimos de selector""")


# def f_se_tablas():
#     """Aqui elegimos la tabla a editar (las tablas son los campos)"""
#     # lo que sigue fue copiado de f_se_columnas
#     print("tablas actuales:")
#     n = 1
#     print("0) salir") 
#     for i in d_co_tablas.keys():
#         print(f"{n}) {i}")
#         n += 1
#     llave = int(input("Elige una tabla a editar: "))
#     if llave == 0:
#         pass
#     else:
#         ds = d_op_tablas[f'{llave}']
#         print(ds)
#         d = d_co_tablas[f'{ds}']
#         print(d)
#         # print("""
#         # a continuacion, optimizador
#         # """)
#         f_se_columnas(llave)
#     print("""
#     ya salimos de selector de tablas""")


# def run():
#     f_se_tablas()
#     print("""
#     informacion a imprimir:
#     """)
#     n = 1
#     for i in d_co_240_subcampos.values():
#         # print(d_op_240[f'{n}'])
#         print(f"{d_op_240[f'{n}']}: {i}")
#         n += 1


# def resultado():
    # lo que viene en adelante creará un documento en sql para exportar:
    file = open("d:/00Eternidad/00Drive/Documentos vivos/Proyectos/Rentabilidad/Base de datos SQL/pkmn/pkmn_datos.sql", "w")
    # lo que sigue será la primera línea del archivo:
    file.write(f"""INSERT INTO `tipos` ({d_op_240['1']})
    VALUES ('{d_co_240_subcampos[d_op_240['1']]}')
    ;""")
    # puedes añadir otra línea bajo la estructura "file.write()". Entre paréntesis debe ir el contenido de la línea:
    # lo que sigue indica que se cierra el archivo:
    file.close()


# if __name__ == '__main__':
#     run()
#     resultado()
#     input()