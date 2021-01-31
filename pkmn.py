"""Función: exportar un documento sql con los cambios a añadir a la base de datos"""


def tabla_tipos_id():
    tipos_id = input("ingresa el id: ")
    t_id = int(input("""guardar?:
    1) sí, guardar e ir a la columna "nombre"
    2) sí, guardar y salir
    3) no, editar
    4) descartar y volver a escoger la columna"""))
    if idt == 1:
        registro['tipos_id'] = tipos_id
        return registro['tipos_id']
        tabla_tipos_nombre()
    elif idt == 2:
        registro['tipos_id'] = tipos_id
        return registro['tipos_id']
    elif idt == 3:
        tabla_tipos_id()
    elif idt == 4:
        tabla_tipos(registro)


def tabla_tipos_nombre():
    tipos_nombre = input("ingresa el nombre: ")
    t_n = int(input("""guardar?:
    1) sí, guardar e ir a la columna "id"
    2) sí, guardar y salir
    3) no, editar
    4) descartar y volver a escoger la columna"""))
    if idt == 1:
        registro['tipos_nombre'] = tipos_nombre
        return registro['tipos_nombre']
        tabla_tipos_id()
    elif idt == 2:
        registro['tipos_nombre'] = tipos_nombre
        return registro['tipos_nombre']
    elif idt == 3:
        tabla_tipos_nombre()
    elif idt == 4:
        tabla_tipos(registro)


def tabla_tipos(registro):
    a = int(input("""Estas en la tabla "tipos", resiona el número correspondiente al campo para editarlo:
    1) id
    2) nombre"""))
    if a == 1:
        tabla_tipos_id()
    elif a == 2:
        tabla_tipos_nombre()
    else:
        print("valor no admisible") 
        tabla_tipos(registro)


def run():
    """esta fórmula permite moverse entre las tablas de la base de datos"""
    registro = {
        'tipos_id': tipos_id,
        'tipos_nombre': tipos_nombre,
    }
    tabla_tipos(registro)
    archivo_resultado()


def archivo_resultado(): 
    # lo que viene en adelante creará un documento en sql para exportar:
    file = open("d:/00Eternidad/00Drive/Documentos vivos/Proyectos/Rentabilidad/Base de datos SQL/pkmn/pkmn_datos.sql", "w")
    # lo que sigue será la primera línea del archivo:
    file.write(f"""INSERT INTO `tipos` (id, nombre)
    VALUES ({registro['tipos_id']}, {registro['tipos_nombre']}""")
    # puedes añadir otra línea bajo la estructura "file.write()". Entre paréntesis debe ir el contenido de la línea:
    # lo que sigue indica que se cierra el archivo:
    file.close()

if __name__ == '__main__':
    run()
    input("")