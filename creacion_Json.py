import json

# modulo que abre archivos de extension csv
def abrir_archivo(nombre_archivo = None):

    try:
        with open(nombre_archivo) as archivo:
            datos_archivo = archivo.readlines()
            print(f"{nombre_archivo} ha sido abierto")
            return datos_archivo
    except FileNotFoundError:
        print("Error, el archivo no fue encontrado")
        quit()

# se modifica determina linea de archivo
def modificar_linea_archivo(linea = None):

    # se pasa a lista
    linea = linea.strip().split(",")
    # se dejan elementos de lista 'linea' que son requeridos, eliminando aquellos que no son utiles
    linea = linea[0:8]
    linea.pop(1)
    linea.pop(5)
    
    # se retorna linea determinada de archivo ya modificada
    return linea

# modulo que evalua si existe correlacion de datos entre determinada linea de archivo 1 con linea de archivo 2
def procesar_datos_archivo2 (archivo_2, pais, fecha):

    fabricante_vacuna = []
    numero_de_vacunas = []
    vacunas_utilizadas = ""

    # linea[0] de archivo 2 corresponde a pais determiando
    # linea[1] de archivo 2 corresponde a fecha determinada de tal pais
    # linea[2] de archivo 2 corresponde al numero de vacunas de determinada fabrica (enunciada en 'linea[3])
    # linea[3] de archivo 2 corresponde al fabricante de vacuna respectivo 

    # se itinera archivo 2
    for linea in archivo_2:
        # se pasa linea de archivo 2 a lista 
        linea = linea.strip().split(",")
        # se datos pais y fecha, pertenecientes a linea de archivo 1, se encuentran tambien en archivo 2
        if linea[0] == pais and linea[1] == fecha:
            # si el numero de vacunas suministradas de determido fabricante no es igual a cero 
            if linea[3] != "0":
                fabricante_vacuna.append(linea[2])
                numero_de_vacunas.append(linea[3])
            else:
                continue
        else:
            continue

    for indice in range (0, len(fabricante_vacuna)):
        vacunas_utilizadas += f"{fabricante_vacuna[indice]}({numero_de_vacunas[indice]}) "
    
    # en acaso de que no haya hubiese informacion de la vacuna utilizada y fabricante
    if fabricante_vacuna == [] and numero_de_vacunas == []:
        vacunas_utilizadas = "Informacion no disponible"

    return vacunas_utilizadas

# modulo que se encarga de procesar los archivos csv, obteniendo la informacion util de tales archivos
def procesar_archivos(archivo, archivo_2):

    total_lineas = len(archivo)
    datos_paises = archivo[1:total_lineas]
    total_lineas -= 1

    # se crea diccionario que contendra data de paises y proceso de vacunacion respectivo
    data_paises = {}

    for linea in range(0,total_lineas):

        # numero absoluto de inmunizaciones = datos_de_pais[2]
        # numero total de vacunados = datos_de_pais[3]
        # numero total de personas con esquema completo = datos_de_pais[4]
        # numero de vacunados ese dia = datos_de_pais[5]

        datos_de_pais = modificar_linea_archivo(datos_paises[linea])
        pais = datos_de_pais[0]
        fecha = datos_de_pais[1] 
        vacunas_utilizadas = procesar_datos_archivo2(archivo_2, pais, fecha)

        for indice in range(2,6):
            if datos_de_pais[indice] == '':
                if indice != 4:
                    datos_de_pais[indice] = 'no existe registro para la fecha'
                else:
                    datos_de_pais[indice] = '0.0'
            else:
                pass
            datos_de_pais[indice] = datos_de_pais[indice].split(".")
            datos_de_pais[indice] = datos_de_pais[indice][0]

        """
        no se logro encontrar informacion para determinar la merma de vacunas
        """

        lista_de_datos = [datos_de_pais[2], datos_de_pais[3], datos_de_pais[4], vacunas_utilizadas, datos_de_pais[5]]

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
    # se crea archivo json que contendra informacion solicitada del proceso de vacunacion en paises
    with open("data_vacunacion.json", "w") as data:
        json.dump(data_paises, data, indent=4)

if __name__ == "__main__":
    main()
