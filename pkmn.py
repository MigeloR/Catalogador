'''el resultado es un documento en sql que sube UNA LINEA de info a la db
etapas:
1) nombre del pkmn en tabla pokemon
2) asociacion del pkmn con sus tipos en pkmn_tipos
2.1) agrega un tipo
2.2) pregunta si tiene segundo tipo
2.2.1) agrega segundo tipo
3) imprime el documento

la información debe agregarse a la lista datos
'''

tipos = {
    '1': 'agua',
    '2': 'acero',
    '3': 'bicho',
    '4': 'fuego',
    '5': 'dragon',
    '6': 'electrico',
    '7': 'fantasma',
    '8': 'hada',
    '9': 'hielo',
    '10': 'lucha',
    '11': 'planta',
    '12': 'normal',
    '13': 'roca',
    '14': 'siniestro',
    '15': 'tierra',
    '16': 'veneno',
    '17': 'volador',
    '18': 'psiquico',
}


datos = []


def pkmn_tipos2():
    # esta funcion añade un segundo tipo
    a = input('escribe el tipo: ')
    # ahora preguntamos si tiene segundo tipo
    datos.append(a)


def pkmn_tipos():
    # esta funcion añade el tipo del pkmn
    counter = 1
    print('estos son los tipos disponibles:')
    for i in tipos.values():
        print(f'{counter}) {i}')
        counter += 1
    a = input('escribe el tipo: ')
    # ahora preguntamos si tiene segundo tipo
    datos.append(a)
    seg = int(input('''tiene segundo tipo?
    0) no
    1) si
    tu respuesta: '''))
    if seg == 1:
        pkmn_tipos2()
    else:
        pass



def nombrepkmn():
    # esta función añade el nombre del pkmn
    b = input('escribe el nombre: ')
    datos.append(b)


def numeropkmn():
    # esta funcion añade el numero del pkmn
    n = int(input('escribe el numero del pkmn: '))
    datos.append(n)


def run():
    numeropkmn()
    nombrepkmn()
    pkmn_tipos()

    imprimir()
    

def imprimir():
    # lo que sigue 'abre' un archivo, entre parentesis se ubica la direccion en donde se creara
    file = open("d:/00Eternidad/00Drive/Documentos vivos/Proyectos/Rentabilidad/Base de datos SQL/pkmn/pkmn_datos.sql", "w")
    # lo que sigue será la primera línea del archivo:
    file.write(f'''
    INSERT INTO pokemon (id, nombre)
    VALUES ('{datos[0]}', '{datos[1]}')
    ;
    INSERT INTO pkmn_tipos (pkmn_id, tipos_id)
    VALUES ('{datos[0]}', '{datos[2]}')
    ;''')
    if len(datos) == 4:
        file.write(f'''
        INSERT INTO pkmn_tipos (pkmn_id, tipos_id)
        ('{datos[0]}', '{datos[3]}')
        ;''')
    else:
        pass
    # puedes añadir otra línea bajo la estructura "file.write()". Entre paréntesis debe ir el contenido de la línea:
    # lo que sigue indica que se cierra el archivo:
    file.close()

if __name__ == '__main__':
    run()