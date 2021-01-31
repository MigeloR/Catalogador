diccionario = {
    'primero': "valor1",
    'segundo': "valor2",
}


def f_primero():
    a = int(input("""quieres dar un valor para PRIMERO?
    1) Yes
    2) No
    ingresa tu respuesta: """))
    if a == 1:
        diccionario['primero'] = input("ingresa un valor para primero: ")
    elif a == 2:
        pass


def f_segundo():
    diccionario['segundo'] = input("ingresa un valor para segundo: ")


def run():
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
    for i in diccionario.values():
        print(i)


if __name__ == '__main__':
    run()