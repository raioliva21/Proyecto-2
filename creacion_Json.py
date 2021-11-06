import json

def procesar_archivo(archivo = None):

    total_lineas = len(archivo) - 1
    datos_paises = archivo[1:total_lineas]

    # se procesa linea a linea el archivo
    # for indice in range(0, len(archivo)):
    for indice in range(0,6):
        if indice == 0:
            print("Linea correspondiente a los indicadores de datos")
            print(archivo[0])
            descripcion_datos = archivo[0]
            descripcion_datos = descripcion_datos.strip().split(",")
        else:
            datos_paises[indice].strip().split(",")
            for subindice in range(0, len(datos_paises[indice])):
                if datos_paises[indice][subindice] == '':
                    #print(f"Se elimina valor de posicion {subindice} en linea {archivo[indice]}")
                    datos_paises[indice].pop(subindice)
                    # se debe concatenar lineas referentes a mismo pais

def abrir_archivo(nombre_archivo = None):

    try:
        with open(nombre_archivo) as archivo:
            datos_archivo = archivo.readlines()
            return datos_archivo
            #print(f"{nombre_archivo} ha sido abierto")
            #return archivo
    except FileNotFoundError:
        print("Error, el archivo no fue encontrado")
        #quit()

def main():
    
    archivo_1 = "country_vaccinations.csv"
    archivo_2 = "country_vaccinations_by_manufacturer.csv"
    datos_archivo_1 = abrir_archivo(archivo_1)
    datos_archivo_2 = abrir_archivo(archivo_2)
    #datos_archivo_1 = procesar_archivo(datos_archivo_1)
    #daots_archivo_2 = procesar_archivo(datos_archivo_2)
    #crear_json(archivo_uno)


if __name__ == "__main__":
    main()