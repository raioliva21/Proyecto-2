import json

def abrir_archivo(nombre_archivo = None):

    try:
        with open(nombre_archivo) as archivo:
            datos_archivo = archivo.readlines()
            print(f"{nombre_archivo} ha sido abierto")
            return datos_archivo
    except FileNotFoundError:
        print("Error, el archivo no fue encontrado")
        quit()


def modificar_archivo(archivo = None):

    archivo = archivo.strip().split(",")
    archivo = archivo[0:8]
    archivo.pop(1)
    archivo.pop(5)
    
    return archivo

def procesar_datos_archivo2 (archivo_2, pais, fecha):

    fabricante_vacuna = []
    numero_de_vacunas = []
    vacunas_utilizadas = ""

    # crear diccionario de archivo_2
    # tal que llaves sean = '{pais}-{fecha} : fabricante_vacuna'

    for linea in archivo_2:
        linea = linea.strip().split(",")
        if linea[0] == pais and linea[1] == fecha:
            if linea[3] != "0":
                fabricante_vacuna.append(linea[2])
                numero_de_vacunas.append(linea[3])
            else:
                continue
        else:
            continue

    for indice in range (0, len(fabricante_vacuna)):
        vacunas_utilizadas += f"{fabricante_vacuna[indice]}({numero_de_vacunas[indice]}) "
    
    if fabricante_vacuna == [] and numero_de_vacunas == []:
        vacunas_utilizadas = "Informacion no disponible"

    print(vacunas_utilizadas)

    return vacunas_utilizadas


def procesar_archivos(archivo, archivo_2):

    total_lineas = len(archivo)
    datos_paises = archivo[1:total_lineas]
    total_lineas -= 1

    data_paises = {}

    for linea in range(0,total_lineas):

        datos_de_pais = modificar_archivo(datos_paises[linea])
        pais = datos_de_pais[0]
        fecha = datos_de_pais[1] 
        vacunas_utilizadas = procesar_datos_archivo2(archivo_2, pais, fecha)


        for indice in range(2,5):
            if datos_de_pais[indice] == '':
                if indice != 4:
                    datos_de_pais[indice] = 'no existe registro para la fecha'
                else:
                    datos_de_pais[indice] = '0.0'
            else:
                pass
            datos_de_pais[indice] = datos_de_pais[indice].split(".")
            datos_de_pais[indice] = datos_de_pais[indice][0]

        # numero absoluto de inmunizaciones = datos_de_pais[2]
        # numero total de vacunados = datos_de_pais[3]
        # numero total de personas con esquema completo = datos_de_pais[4]
        # numero de vacunados ese dia = datos_de_pais[5]

        lista_de_datos = [datos_de_pais[2], datos_de_pais[3], datos_de_pais[4], datos_de_pais[5], vacunas_utilizadas ]

        data_paises.update ({f"{pais}-{fecha}" : lista_de_datos})

    return data_paises


def main():
    
    #archivo_1 = "country_vaccinations.csv"
    archivo_1 = "/home/raimundoosf/Escritorio/Python/En clases/Proyecto N°2/country_vaccinations.csv"
    #archivo_2 = "country_vaccinations_by_manufacturer.csv"
    archivo_2 = "/home/raimundoosf/Escritorio/Python/En clases/Proyecto N°2/country_vaccinations_by_manufacturer.csv"
    datos_archivo_1 = abrir_archivo(archivo_1)
    datos_archivo_2 = abrir_archivo(archivo_2)
    data_paises = procesar_archivos(datos_archivo_1, datos_archivo_2)
    with open("data_vacunacion.json", "w") as data:
        json.dump(data_paises, data, indent=4)

if __name__ == "__main__":
    main()
