diccionario = {
    'primero': "valor1",
    'segundo': "valor2",
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


def selector():
    a = int(input("""elige una de las opciones:
    1) editar PRIMERO
    2) editar SEGUNDO
    3) no editar nada, imprimir lo que hay
    """))
    if a == 1:
        f_primero()
    elif a == 2:
        f_segundo()
    elif a == 3:
        pass


def run():
    selector()
    print("""
    informacion a imprimir: """)
    for i in diccionario.values():
        print(i)


if __name__ == '__main__':
    run()
    # input()