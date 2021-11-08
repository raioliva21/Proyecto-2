import json

#def procesar_datos_paises(datos_paises):

def eliminar_datos_inutiles(archivo = None):

    archivo = archivo.strip().split(",")
    archivo = archivo[0:8]
    archivo.pop(1)
    archivo.pop(5)
    
    return archivo

def procesar_archivos(archivo, archivo_2):

    print("\n")

    total_lineas = len(archivo) - 1
    variables_descriptivas = archivo[0]
    datos_paises = archivo[1:total_lineas]

    variables_descriptivas = eliminar_datos_inutiles(variables_descriptivas)
    print(variables_descriptivas)
    print("\n")


    data_paises = {}
    data_paises['paises'] = []
    print(type(data_paises))
    

    for linea in range(0,1):

        datos_de_pais = eliminar_datos_inutiles(datos_paises[linea])
        print("'dato_pais_' es de tipo : ", end = "")
        print(type(datos_de_pais))
        pais = datos_de_pais[0]
        fecha = datos_de_pais[1] 
        fecha = fecha.strip().split("-")
        anio = fecha[0]
        mes = fecha[1]
        dia = fecha[2]

        print(type(datos_de_pais[2]))

        for indice in range(2,5):
            if datos_de_pais[indice] == '0.0':
                datos_de_pais[indice] = 'no existe registro para la fecha'
            else:
                pass
            

        num_absoluto_inmunizaciones = datos_de_pais[2]
        num_total_vacunados = datos_de_pais[3]
        num_total_personas_con_esquema_completo = datos_de_pais[4]

        lista_de_datos = [num_absoluto_inmunizaciones, num_total_vacunados , num_total_personas_con_esquema_completo]

        data_paises.update ({f"{pais}-{anio}-{mes}-{dia}" : lista_de_datos})

        #print("se imprimen los datos de pais")
        #print(data_paises[f"{pais}-{anio}-{mes}-{dia}"][0])



def abrir_archivo(nombre_archivo = None):

    try:
        with open(nombre_archivo) as archivo:
            datos_archivo = archivo.readlines()
            print(f"{nombre_archivo} ha sido abierto")
            return datos_archivo
    except FileNotFoundError:
        print("Error, el archivo no fue encontrado")
        quit()


def main():
    
    archivo_1 = "country_vaccinations.csv"
    archivo_1 = "/home/raimundoosf/Escritorio/Python/En clases/Proyecto N°2/country_vaccinations.csv"
    archivo_2 = "/home/raimundoosf/Escritorio/Python/En clases/Proyecto N°2/country_vaccinations_by_manufacturer.csv"
    datos_archivo_1 = abrir_archivo(archivo_1)
    datos_archivo_2 = abrir_archivo(archivo_2)
    procesar_archivos(datos_archivo_1, datos_archivo_2)
    #datos_archivo_2 = procesar_archivo(datos_archivo_2)
    #crear_json(archivo_uno)


if __name__ == "__main__":
    main()
    
    archivo_1 = "country_vaccinations.csv"
    archivo_2 = "country_vaccinations_by_manufacturer.csv"
    datos_archivo_1 = abrir_archivo(archivo_1)
    datos_archivo_2 = abrir_archivo(archivo_2)
    #datos_archivo_1 = procesar_archivo(datos_archivo_1)
    #daots_archivo_2 = procesar_archivo(datos_archivo_2)
    #crear_json(archivo_uno)


if __name__ == "__main__":
    main()
