'''el resultado es un documento en sql que sube info a la db
etapas:
1) nombre del pkmn en tabla pokemon
2) asociacion del pkmn con sus tipos en pkmn_tipos
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


def pkmn_tipos():
    a = input('escribe el tipo: ')


def nombrepkmn():
    b = input('escribe el nombre: ')


def run():
    nombrepkmn()
    pkmn_tipos()
    imprimir()
    

def imprimir():
    # lo que sigue 'abre' un archivo, entre parentesis se ubica la direccion en donde se creara
    file = open("d:/00Eternidad/00Drive/Documentos vivos/Proyectos/Rentabilidad/Base de datos SQL/pkmn/pkmn_datos.sql", "w")
    # lo que sigue será la primera línea del archivo:
    file.write(f'''nombre y tipo''')
    # puedes añadir otra línea bajo la estructura "file.write()". Entre paréntesis debe ir el contenido de la línea:
    # lo que sigue indica que se cierra el archivo:
    file.close()

if __name__ == '__main__':
    run()