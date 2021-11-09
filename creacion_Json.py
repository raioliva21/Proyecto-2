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


def eliminar_datos_inutiles(archivo = None):

    archivo = archivo.strip().split(",")
    archivo = archivo[0:8]
    archivo.pop(1)
    archivo.pop(5)
    
    return archivo

def procesar_archivos(archivo, archivo_2):

    total_lineas = len(archivo)
    datos_paises = archivo[1:total_lineas]
    total_lineas -= 1

    data_paises = {}

    for linea in range(0,total_lineas):

        datos_de_pais = eliminar_datos_inutiles(datos_paises[linea])
        pais = datos_de_pais[0]
        fecha = datos_de_pais[1] 
        fecha = fecha.strip().split("-")
        anio = fecha[0]
        mes = fecha[1]
        dia = fecha[2]

        for indice in range(2,5):
            if datos_de_pais[indice] == '':
                datos_de_pais[indice] = 'no existe registro para la fecha'
            else:
                pass

        num_absoluto_inmunizaciones = datos_de_pais[2]
        num_total_vacunados = datos_de_pais[3]
        num_total_personas_esq_completo = datos_de_pais[4]
        num_vacunados_ese_dia = datos_de_pais[5]

        lista_de_datos = [num_absoluto_inmunizaciones, num_total_vacunados, num_total_personas_esq_completo, num_vacunados_ese_dia]

        data_paises.update ({f"{pais}-{anio}-{mes}-{dia}" : lista_de_datos})

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
