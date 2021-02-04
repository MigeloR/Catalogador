d_op_columnas = {
    '1': "titulo de la obra",
    '2': "nombre del autor",
    '3': "Fecha de publicacion",
}


d_co_columnas = {
    'titulo de la obra': "",
    'nombre del autor': "",
    'Fecha de publicacion': ""
}


def optimizador(ds):
    print("estado actual:")
    n = 1
    for i in d_co_columnas.values():
        # print(d_op_columnas[f'{n}'])
        print(f"{d_op_columnas[f'{n}']}: {i}")
        n += 1
    print("")
    d_co_columnas[f'{ds}'] = input(f"escribe un valor para {ds}: ")
    print("")
    selector()

    
# def optimizador(ds):
#     print("estado actual:")
#     for i in d_co_columnas.values():
#         print(i)
#     print("")
#     d_co_columnas[f'{ds}'] = input(f"escribe un valor para {ds}:")
#     selector()        


def selector():
    """Aqui se escogera un valor y este determinara la llave a editar"""
    print("campos actuales:")
    n = 1
    print("0) salir") 
    for i in d_co_columnas.keys():
        print(f"{n}) {i}")
        n += 1
    llave = int(input("Elige una campo a editar: "))
    if llave == 0:
        pass
    else:
        ds = d_op_columnas[f'{llave}']
        print(ds)
        d = d_co_columnas[f'{ds}']
        print(d)
        # print("""
        # a continuacion, optimizador
        # """)
        optimizador(ds)
    print("""
    ya salimos de selector""")


def run():
    selector()
    print("""
informacion a imprimir:
""")
    n = 1
    for i in d_co_columnas.values():
        # print(d_op_columnas[f'{n}'])
        print(f"{d_op_columnas[f'{n}']}: {i}")
        n += 1


def resultado():
    # lo que viene en adelante creará un documento en sql para exportar:
    file = open("d:/00Eternidad/00Drive/Documentos vivos/Proyectos/Rentabilidad/Base de datos SQL/pkmn/pkmn_datos.sql", "w")
    # lo que sigue será la primera línea del archivo:
    file.write(f"""INSERT INTO `tipos` ({d_op_columnas['1']})
    VALUES ('{d_co_columnas[d_op_columnas['1']]}')
    ;""")
    # puedes añadir otra línea bajo la estructura "file.write()". Entre paréntesis debe ir el contenido de la línea:
    # lo que sigue indica que se cierra el archivo:
    file.close()


if __name__ == '__main__':
    run()
    resultado()
    input()