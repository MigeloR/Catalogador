dic_selector = {
    '1': "nombre",
}

t_tipos = {
    'nombre': "",
}


def optimizador(ds):
    print("estado actual:")
    for i in t_tipos.values():
        print(i)
    print("")
    t_tipos[f'{ds}'] = input(f"escribe un valor para {ds}:")
    selector()

        


def selector():
    """Aqui se escogera un valor y este determinara la llave a editar"""
    print("campos actuales:")
    n = 1
    print("0) salir") 
    for i in t_tipos.keys():
        print(f"{n}) {i}")
        n += 1
    llave = int(input("Elige una campo a editar: "))
    if llave == 0:
        pass
    else:
        ds = dic_selector[f'{llave}']
        print(ds)
        d = t_tipos[f'{ds}']
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
    informacion a imprimir: """)
    for i in t_tipos.values():
        print(i)


def resultado():
    # lo que viene en adelante creará un documento en sql para exportar:
    file = open("d:/00Eternidad/00Drive/Documentos vivos/Proyectos/Rentabilidad/Base de datos SQL/pkmn/pkmn_datos.sql", "w")
    # lo que sigue será la primera línea del archivo:
    file.write(f"""INSERT INTO `tipos` ({dic_selector['1']})
    VALUES ('{t_tipos[dic_selector['1']]}')
    ;""")
    # puedes añadir otra línea bajo la estructura "file.write()". Entre paréntesis debe ir el contenido de la línea:
    # lo que sigue indica que se cierra el archivo:
    file.close()


if __name__ == '__main__':
    run()
    resultado()
    input()