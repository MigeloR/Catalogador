lista = []
tupla = ()
diccionario = {}


def run():
    print(f'''entrando a run; así se ve la lista:
    {lista}''')
    lista.append(1)
    print(f'''saliendo de run; así se ve la lista:
    {lista}''')



if __name__ == '__main__':
    print(f'''''empieza la función; así se ve la lista:
    {lista}''')
    run()
    print(f'''termina la función; así se ve la lista:
    {lista}''')
