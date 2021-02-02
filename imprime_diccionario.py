dic_selector = {
    '1': "id",
    '2': "nombre",
}

diccionario = {
    'id': "",
    'nombre': "",
}


def f_primero():
    b = int(input("""quieres dar un valor para PRIMERO?
    1) Yes
    2) No
    ingresa tu respuesta: """))
    if b == 1:
        diccionario['primero'] = input("ingresa un valor para primero: ")
        print("""
        valores actuales:""")
        for i in diccionario.values():
            print(i)
        print("")
        # Aqui finaliza esta funcion
        pass
        
        # Ahora quiero ir a selector:
        selector()
    elif b == 2:
        pass
    # # revisando diccionario
    # for i in diccionario.values():
    #     print("despues de todo")
    #     print(i)


    # diccionario['primero'] = input("ingresa un valor para primero: ")


def f_segundo():
    b = int(input("""quieres dar un valor para SEGUNDO?
    1) Yes
    2) No
    ingresa tu respuesta: """))
    if b == 1:
        diccionario['segundo'] = input("ingresa un valor para segundo: ")
        print("""
        valores actuales:""")
        for i in diccionario.values():
            print(i)
        print("")
        # Aqui finaliza esta funcion
        pass
        
        # Ahora quiero ir a selector:
        selector()
    elif b == 2:
        pass
    # # revisando diccionario
    # for i in diccionario.values():
    #     print("despues de todo")
    #     print(i)


def optimizador(ds):
    print("estado actual:")
    for i in diccionario.values():
        print(i)
    print("")
    diccionario[f'{ds}'] = input(f"escribe un valor para {ds}:")
    selector()

        


def selector():
    """Aqui se escogera un valor y este determinara la llave a editar"""
    print("campos actuales:")
    n = 1
    print("0) salir") 
    for i in diccionario.keys():
        print(f"{n}) {i}")
        n += 1
    llave = int(input("Elige una campo a editar: "))
    if llave == 0:
        pass
    else:
        ds = dic_selector[f'{llave}']
        print(ds)
        d = diccionario[f'{ds}']
        print(d)
        print("""
        a continuacion, optimizador
        """)
        optimizador(ds)
    print("""
    ya salimos de selector""")

    
    # optimizador(llave)
    
    # # funcion antigua:
    # a = int(input("""elige una de las opciones:
    # 1) editar PRIMERO
    # 2) editar SEGUNDO
    # 3) no editar nada, imprimir lo que hay
    # """))
    # if a == 1:
    #     f_primero()
    # elif a == 2:
    #     f_segundo()
    # elif a == 3:
    #     pass
    # funcion nueva:


def run():
    selector()
    print("""
    informacion a imprimir: """)
    for i in diccionario.values():
        print(i)


def resultado():
    # lo que viene en adelante creará un documento en sql para exportar:
    file = open("d:/00Eternidad/00Drive/Documentos vivos/Proyectos/Rentabilidad/Base de datos SQL/pkmn/pkmn_datos.sql", "w")
    # lo que sigue será la primera línea del archivo:
    file.write(f"""INSERT INTO `tipos` ({dic_selector['1']}, {dic_selector['2']})
    VALUES ({diccionario[dic_selector['1']]}, {diccionario[dic_selector['2']]})""")
    # puedes añadir otra línea bajo la estructura "file.write()". Entre paréntesis debe ir el contenido de la línea:
    # lo que sigue indica que se cierra el archivo:
    file.close()


if __name__ == '__main__':
    run()
    resultado()
    input()