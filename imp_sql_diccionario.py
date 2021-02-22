# Proceso:
# 1) run()
# 1.1) escoge_campo()
# 1.1.1) dirige_a_escoge_subcampos()
# 1.1.1.1) escoge_subcampo()
# 2) imprimir()
# 


elegir_240 = {
    '1': '$a_Titulo_uniforme_NR',
    '2': '$d_Fecha_de_la_firma_de_un_tratado_R',
    '3': '$f_Fecha_de_la_obra_NR',
    '4': '$g_Informacion_miscelanea_R',
    '5': '$k_Subencabezamiento_de_forma_R',
    '6': '$l_Lengua_de_la_obra_NR',
    '7': '$m_Medio_de_interpretacion_R',
    '8': '$n_Numero_de_parte_o_seccion_de_la_obra_R',
    '9': '$o_Arreglo_NR',
    '10': '$p_Nombre_de_parte_o_seccion_de_la_obra_R',
    '11': '$r_Tonalidad_NR',
    '12': '$s_Version_R',
    '13': '$6_Enlace_NR',
}


llenar_subcampos_240 = {
    '$a_Titulo_uniforme_NR': "",
    '$d_Fecha_de_la_firma_de_un_tratado_R': "",
    '$f_Fecha_de_la_obra_NR': "",
    '$g_Informacion_miscelanea_R': "",
    '$k_Subencabezamiento_de_forma_R': "",
    '$l_Lengua_de_la_obra_NR': "",
    '$m_Medio_de_interpretacion_R': "",
    '$n_Numero_de_parte_o_seccion_de_la_obra_R': "",
    '$o_Arreglo_NR': "",
    '$p_Nombre_de_parte_o_seccion_de_la_obra_R': "",
    '$r_Tonalidad_NR': "",
    '$s_Version_R': "",
    '$6_Enlace_NR': "",
}


elegir_245 = {
    '1': '$a Título (NR)',
    '2': '$c Mención de responsabilidad, etc. (NR)',
    '3': '$f Fechas extremas (NR)',
    '4': '$g Fechas predominantes (NR)',
    '5': '$k Forma (R)',
    '6': '$n_Numero_de_parte_o_seccion_de_la_obra_(R)',
    '7': '$p_Nombre_de_parte_o_seccion_de_la_obra_(R)',
    '8': '$s Versión (NR)',
    '9': '$6_Enlace_(NR)',
}


llenar_subcampos_245 = {
    '$a Título (NR)': "",
    '$c Mención de responsabilidad, etc. (NR)': "",
    '$f Fechas extremas (NR)': "",
    '$g Fechas predominantes (NR)': "",
    '$k Forma (R)': "",
    '$n_Numero_de_parte_o_seccion_de_la_obra_(R)': "",
    '$p_Nombre_de_parte_o_seccion_de_la_obra_(R)': "",
    '$s Versión (NR)': "",
    '$6_Enlace_(NR)': "",    
}


elegir_campos = {
    '1': "240_titulo_uniforme_nr",
    '2': "245_Mencion_de_titulo",
}


llenar_campos = {
    '240_titulo_uniforme_nr': elegir_240,
    '245_Mencion_de_titulo': elegir_245,
}


llenar_subcampos_XXX = {
    '240_titulo_uniforme_nr': llenar_subcampos_240,
    '245_Mencion_de_titulo': llenar_subcampos_245,
}


def escoge_subcampos(lss,ivlc):
    subcampo_elegido = int(input("""
    elige un subcampo: """))
    # print(f"""
    # este es el subcampo elegido: {subcampo_elegido}; {ivlc[f"{subcampo_elegido}"]}""")       
    para_lss = ivlc[f"{subcampo_elegido}"]
    # print(f"""
    # esto es para_lss: {ivlc[f"{subcampo_elegido}"]}""")
    # print(f"""
    # esto es para_lss en lss: {lss[para_lss]}""")
    lss[para_lss] = input(f"""agrega un contenido para {ivlc[f'{subcampo_elegido}']}: 
    """)
    print("")

    # aqui preguntamos si quiere editar otro subcampo:
    otro = int(input("""editar otro subcampo?
    0 = no
    1 = si"""))
    if otro == 0:
        pass
    elif otro == 1:
        escoge_subcampos(lss,ivlc)
    
    
def dirige_a_escoge_subcampos(lss,ivlc):
    """aqui se muestran los subcampos del campo elegido y se escoge uno"""
    print("""
    aqui empieza la seleccion de subcampos
    """)
    n = 1
    for i in ivlc.values():
        print(f"{n}) {i}")
        n += 1
    escoge_subcampos(lss,ivlc)
    

def escoge_campo():
    """aqui escogeremos un campo"""
    n = 1
    print("campos disponibles:")
    for i in elegir_campos.values():
        print(f"{n}) {i}")
        n += 1
    campo_elegido = int(input("""
    elgie un campo: """))
    # print(f"""
    # elegiste la opcion: {campo_elegido}""")
    
    # campo elegido en llenar_campos:
    celc = elegir_campos[f'{campo_elegido}']
    # print(f"""
    # celc: {celc}; celc es tipo: {type(celc)}""")
    # print(f"""
    # esta opcion es el campo: {elegir_campos[f'{campo_elegido}']}""")
    
    # imprimiendo los valores de llenar_campos:
    ivlc = llenar_campos[f'{celc}']
    # print(f"""
    # este es el valor de ivlc: {ivlc} y es de tipo: {type(ivlc)}""")
    
    # llenaremos los subcampos del subcampo_XXX:
    lss = llenar_subcampos_XXX[celc]
    # print(f"""
    # lss tiene: {lss}""")
    
    # nos vamos a escoger un subcampo:
    dirige_a_escoge_subcampos(lss,ivlc)
    
    # aniadido al final, si no sirve, crear un campo "dirige_a_elegir_campo":
    otro_campo = int(input("""
    quieres editar otro campo?
    0 = no
    1 = si"""))
    if otro_campo == 0:
        pass
    elif otro_campo == 1:
        escoge_campo()
    


def run():
    escoge_campo()


def imprimir():
    """previsualizacion de lo que se exportara"""
    n = 0
    lista_llenar_subcampos_240_llaves = []
    lista_llenar_subcampos_240_valores = []
    for i in llenar_subcampos_240.keys():
        n += 1
        if llenar_subcampos_240[f'{i}'] == "":
            continue
        else:
            # print(f"{n}) {i}: {llenar_subcampos_240[f'{i}']}")
            lista_llenar_subcampos_240_llaves.append(i)
            lista_llenar_subcampos_240_valores.append(llenar_subcampos_240[f'{i}'])
    lista_llenar_subcampos_240_llaves = tuple(lista_llenar_subcampos_240_llaves)
    lista_llenar_subcampos_240_valores = tuple(lista_llenar_subcampos_240_valores)
    print(lista_llenar_subcampos_240_llaves)
    print(lista_llenar_subcampos_240_valores)
    archivo(lista_llenar_subcampos_240_llaves,lista_llenar_subcampos_240_valores)


# # # def resultado():
# # #     """aqui estara la estructura de lo que se exportara"""
# # #     # lo que viene en adelante creará un documento en sql para exportar:
# # #     file = open("d:/00Eternidad/00Drive/Documentos vivos/Proyectos/Rentabilidad/Base de datos SQL/pkmn/pkmn_datos.sql", "w")
# # #     # lo que sigue será la primera línea del archivo:
# # #     file.write(f"""INSERT INTO `{llenar_subcampos_240}` (lista_llenar_subcampos_240_llaves)
# # #     VALUES ({lista_llenar_subcampos_240_valores}""")
# # #     # puedes añadir otra línea bajo la estructura "file.write()". Entre paréntesis debe ir el contenido de la línea:
# # #     # lo que sigue indica que se cierra el archivo:
# # #     file.close()


def temporal(lista_llenar_subcampos_240_llaves):
    ex = len(lista_llenar_subcampos_240_llaves)
    n = 0
    for i in lista_llenar_subcampos_240_llaves:
        n += 1
        if ex - n == 0:
            print(f"{i}")
        else:
            print(f"{i},")



def archivo(lista_llenar_subcampos_240_llaves,lista_llenar_subcampos_240_valores):
    """aqui se redactara el archivo que se exportara"""
    # primero, determinar las columnas (subcampos) a llenar:
    print("imprimiendo a y b")
    # esto es temporal:
    """aqui estara la estructura de lo que se exportara"""
    # lo que viene en adelante creará un documento en sql para exportar:
    file = open("d:/00Eternidad/00Drive/Documentos vivos/Proyectos/Rentabilidad/Base de datos SQL/pkmn/marc21_datos.sql", "w")
    # lo que sigue será la primera línea del archivo:
    ## lo que hace falta aqu'i es cambiar ''lista_llenar_subcampos_240_llaves'' por las llaves, para que el resultado sea el mismo que 'INSERT INTO `elegir_campos...`'
    ## quiz'a convenga hacer un 'archivo()' por cada area que seria llenada
    file.write(f"""INSERT INTO `{elegir_campos[f'{1}']}` {lista_llenar_subcampos_240_llaves}
    VALUES {lista_llenar_subcampos_240_valores};""")
    # puedes añadir otra línea bajo la estructura "file.write()". Entre paréntesis debe ir el contenido de la línea:
    # lo que sigue indica que se cierra el archivo:
    file.close()

    # resultado() aqui deberia estar

   


if __name__ == '__main__':
    # la funcion run() inicia todo
    run()
    imprimir()
    # archivo() se supone que aqui deberia ir
    input()
