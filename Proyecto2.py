import json

def abrir_archivo_json():

    try:
        with open("/home/raimundoosf/Escritorio/Python/En clases/data_vacunacion.json", "r") as archivo_json:
            data_vacunacion = json.load(archivo_json)
            return data_vacunacion
    except FileNotFoundError:
        print("Error, el archivo no fue encontrado")
        quit()

def menu():

    while True:
        try:
            print(">> Registro global de tasas de vacunacion COVID-19 <<")
            print("<1> para consultar por totalidad de reportes mensuales en determinado pais.")
            print("<2> para consulta especficia de pais y fecha determinada.")
            decision_usuario = int(input(("<3> para comparar dos paises en un dia, mes o año especifico.\n")))
            if 4 > decision_usuario and decision_usuario > 0:
                break
        except ValueError :
            print("Error, valor ingresado no pertenece a un entero")
            continue

    return decision_usuario

def ingreso_de_datos_a_consultar(solicitar_comparacion, numero_pais_a_consultar):

    anio = None
    mes = None
    dia = None

    while True:
        try:
            if solicitar_comparacion == False:
                pais = input("Seleccione el pais a mostrar: ")
                print("\n")
            else:
                if numero_pais_a_consultar == 1:
                    pais = input("Ingrese pais a comparar: ")
                else:
                    pais = input("Ingrese pais por el cual: ")
            pais = pais.lower()
            pais = pais.capitalize()
            if type(pais) == str:
                break
        except ValueError:
            print("Error, valor ingresado no corresponde a cadena de caracteres (palabra(s))")
            continue
    
    if numero_pais_a_consultar == 1 and solicitar_comparacion == True or numero_pais_a_consultar == 2:
        print("Se solicitara fecha especifica a consultar.")
        while True:
            anio = input("Año: ")
            mes = input("Mes: ")
            dia = input("Dia: ")
            print("\n")
            if anio.isdigit():
                if mes.isdigit() and len(mes) == 2:
                    if dia.isdigit() and len(dia) == 2:
                        break
                    else:
                        print("Error, ingreso de dia debe ser en numero de dos digitos. Ej: 'Dia: 04'")
                else:
                    print("Error, ingreso de mes debe ser en numero de dos digitos. Ej: 'Mes: 04'")
            else:
                print("Error, ingreso de anio debe ser en numero. Ej: 'Anio: 2021'")

    return pais, anio, mes, dia

def convertir_a_str(dato = None):

	dato = str(dato)
	if len(dato) == 1:
		dato = "0" + dato
	else:
		pass
    
	return dato

def evaluar_fecha(anio, mes, dia, registro_encontrado):

    mes = int(mes)
    dia = int(dia)

    if anio == 2020 and mes == 12 and dia == 27 or anio == 2020 and mes == 12 and registro_encontrado == True:
        anio = 2021
        mes = 0
        dia = 32

    return anio, mes, dia

def imprimir_data_pais(data_vacunacion, pais, anio, mes, dia, decision_usuario):

    #print(f"{pais}-{anio}-{mes}-{dia}")

    if f"{pais}-{anio}-{mes}-{dia}" in data_vacunacion:
        if decision_usuario == 1:
            print(f"Anio: {anio}")
            print(f"Mes: {int(mes)}")
        else:
            print(f"{pais}:")
            print(f"Numero de personas vacunadas aquel dia: {data_vacunacion[f'{pais}-{anio}-{mes}-{dia}'][3]}")
        print(f"Numero absoluto de inmunizaciones: {data_vacunacion[f'{pais}-{anio}-{mes}-{dia}'][0]}")
        print(f"Numero total de personas vacunadas: {data_vacunacion[f'{pais}-{anio}-{mes}-{dia}'][1]}")
        print(f"Numero total de personas con el esquema completo: {data_vacunacion[f'{pais}-{anio}-{mes}-{dia}'][2]}\n")
        #print(f"Vacuna utilizada: {}")
        #print(f"Merma de vacunas: {}")
    else:
        print("Error. Datos para pais con fecha respectiva no han sido encontrados.")

def procesar_decision_usuario(decision_usuario, data_vacunacion):


    if decision_usuario == 1:

        solicitar_comparacion = False
        numero_pais_a_consultar = None

        pais, anio, mes, dia = ingreso_de_datos_a_consultar(solicitar_comparacion, numero_pais_a_consultar)
        
        anio = 2020
        mes = 0
        registro_encontrado = None

        print(f"{pais}")
        while mes != 13:
            mes += 1
            for dia in range(32,26,-1):
                mes = convertir_a_str(mes)
                dia = convertir_a_str(dia)
                if f"{pais}-{anio}-{mes}-{dia}" in data_vacunacion:
                    if data_vacunacion[f"{pais}-{anio}-{mes}-{dia}"][0] != 'no existe registro para la fecha':
                        imprimir_data_pais(data_vacunacion, pais, anio, mes, dia, decision_usuario)
                        registro_encontrado = True
                        anio, mes, dia = evaluar_fecha(anio, mes, dia, registro_encontrado)
                        break
                    else:
                        registro_encontrado = False
                        anio, mes, dia = evaluar_fecha(anio, mes, dia, registro_encontrado)
                else:
                    registro_encontrado = False    
                    anio, mes, dia = evaluar_fecha(anio, mes, dia, registro_encontrado)

    if decision_usuario == 2:

        solicitar_comparacion = False
        numero_pais_a_consultar = None
        pais, anio, mes, dia = ingreso_de_datos_a_consultar(solicitar_comparacion, numero_pais_a_consultar)
        imprimir_data_pais(data_vacunacion, pais, anio, mes, dia, decision_usuario)
    
    if decision_usuario == 3:
        
        solicitar_comparacion = True
        numero_pais_a_consultar = 1
        pais_uno, anio, mes, dia = ingreso_de_datos_a_consultar(solicitar_comparacion, numero_pais_a_consultar)
        numero_pais_a_consultar = 2
        pais_dos, anio, mes, dia = ingreso_de_datos_a_consultar(solicitar_comparacion, numero_pais_a_consultar)
        imprimir_data_pais(data_vacunacion, pais_uno, anio, mes, dia, decision_usuario)
        imprimir_data_pais(data_vacunacion, pais_dos, anio, mes, dia, decision_usuario)


def main():
    data_vacunacion = abrir_archivo_json()
    decision_usuario = menu()
    procesar_decision_usuario(decision_usuario, data_vacunacion)

if __name__ == "__main__":
    main()
