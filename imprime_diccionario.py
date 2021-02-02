dic_selector = {
    '1': "id",
    '2': "nombre",
}

diccionario = {
    'id': "valor1",
    'nombre': "valor2",
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
        


def selector():
    """Aqui se escogera un valor y este determinara la llave a editar"""
    print("campos actuales:")
    n = 1 
    for i in diccionario.keys():
        print(f"{n}) {i}")
        n += 1
    llave = int(input("Elige una campo a editar: "))
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


if __name__ == '__main__':
    run()
    # input()