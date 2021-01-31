"""Función: exportar un documento sql con los cambios a añadir a la base de datos"""


def run():
    archivo_resultado()


def archivo_resultado(): 
    # lo que viene en adelante creará un documento en sql para exportar:
    file = open("d:/00Eternidad/00Drive/Documentos vivos/Proyectos/Rentabilidad/Base de datos SQL/pkmn/pkmn_datos.sql", "w")
    # lo que sigue será la primera línea del archivo:
    file.write("""Aquí va el contenido de esta línea""")
    # puedes añadir otra línea bajo la estructura "file.write()". Entre paréntesis debe ir el contenido de la línea:
    # lo que sigue indica que se cierra el archivo:
    file.close()

if __name__ == '__main__':
    run()
    input("")