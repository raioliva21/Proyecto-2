import json

# se abre archivo json
def abrir_archivo_json():

    try:
        with open("/home/raimundoosf/Escritorio/Python/En clases/data_vacunacion.json", "r") as archivo_json:
            data_vacunacion = json.load(archivo_json)
            return data_vacunacion
    except FileNotFoundError:
        print("Error, el archivo no fue encontrado")
        quit()

# menu principal, donde usuario deccide por que item consultar 
def menu():

    # se esta en bucle hasta que valores ingresados por usuario sean aceptados
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

# funcion en donde se solicita a usuario ingresar determinados datos dependiendo de la decision tomada previamente
def ingreso_de_datos_a_consultar(decision_usuario, numero_pais_a_consultar):

    anio = None
    mes = None
    dia = None

    while True:
        try:
            # en caso de que decision de usuario haya sido 1 o 2 (no comparar entre paises)
            if decision_usuario != 3:
                pais = input("Seleccione el pais a mostrar: ")
                print("\n")
            # si opcion de usuario fue 3; comparar entre paises 
            else:
                # si es que se pregunta por el 1er pais (pais a comparar)
                if numero_pais_a_consultar == 1:
                    pais = input("Ingrese pais a comparar: ")
                else:
                    pais = input("Ingrese pais por el cual comparar: ")
            # se adapta formato de 'pais'
            pais = pais.lower()
            pais = pais.capitalize()
            if type(pais) == str:
                break
        except ValueError:
            print("Error, valor ingresado no corresponde a cadena de caracteres (palabra(s))")
            continue
    
    if decision_usuario == 2 or decision_usuario == 3 and numero_pais_a_consultar == 2:
        print("Se solicitara fecha especifica a consultar.")
        while True:
            anio = input("Año: ")
            mes = input("Mes: ")
            dia = input("Dia: ")
            print("\n")
            if anio.isdigit() and len(anio) == 4:
                if mes.isdigit():
                    if len(mes) == 1:
                        mes = '0' + mes
                    if len(mes) != 2:
                        print("Error, se debe ingresar numero entre uno y dos digitos.")
                        continue
                    if dia.isdigit() and len(dia) == 2:
                        break
                    else:
                        if dia.isdigit() and len(dia) == 1:
                            dia = "0" + dia
                            break
                        else:
                            print("Error, se debe ingresar numero entre uno y dos digitos.")
                            continue
                else:
                    print("Error, se debe ingresar valor numerico. Ej: 'Mes: 11")
            else:
                print("Error, ingreso de anio debe ser en numero. Ej: 'Anio: 2021'")
                continue

    return pais, anio, mes, dia

def convertir_a_str(dato = None):

	dato = str(dato)
	if len(dato) == 1:
		dato = "0" + dato
	else:
		pass
    
	return dato

# modulo que cambia fecha en caso de que se tenga el mes 12 en anio 2020, evitando cierre de cilo en modulo de donde se llama
def evaluar_fecha(anio, mes, dia, registro_encontrado):

    mes = int(mes)
    dia = int(dia)

    if anio == 2020 and mes == 12 and dia == 27 or anio == 2020 and mes == 12 and registro_encontrado == True:
        anio = 2021
        mes = 0
        dia = 32

    return anio, mes, dia

# modulo que imprime datos solicitados dependiente de la decision de usuario en menu
def imprimir_data_pais(data_vacunacion, pais, anio, mes, dia, decision_usuario):

    if f"{pais}-{anio}-{mes}-{dia}" in data_vacunacion:
        if decision_usuario == 1:
            print(f"Anio: {anio}")
            print(f"Mes: {int(mes)}")
        else:
            print(f"{pais}:")
            print(f"Numero de personas vacunadas aquel dia: {data_vacunacion[f'{pais}-{anio}-{mes}-{dia}'][4]}")
        print(f"Numero absoluto de inmunizaciones: {data_vacunacion[f'{pais}-{anio}-{mes}-{dia}'][0]}")
        print(f"Numero total de personas vacunadas: {data_vacunacion[f'{pais}-{anio}-{mes}-{dia}'][1]}")
        print(f"Numero total de personas con el esquema completo: {data_vacunacion[f'{pais}-{anio}-{mes}-{dia}'][2]}")
        print(f"Vacuna utilizada: {data_vacunacion[f'{pais}-{anio}-{mes}-{dia}'][3]}\n")
        #print(f"Merma de vacunas: {}")
    else:
        print("Error. Datos para pais con fecha respectiva no han sido encontrados.")

def procesar_decision_usuario(decision_usuario, data_vacunacion):

    if decision_usuario == 1:

        # siguinte variable adquiere valor nulo, pues es util cuando decision de usuario es 3 (comparacion entre paises)
        numero_pais_a_consultar = None

        pais, anio, mes, dia = ingreso_de_datos_a_consultar(decision_usuario, numero_pais_a_consultar)
        
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
                        # se evalua fecha en caso de que se este en mes 12 del año 2020, tal que se evite cierre de ciclo 'for'
                        anio, mes, dia = evaluar_fecha(anio, mes, dia, registro_encontrado)
                        break
                    else:
                        registro_encontrado = False
                        anio, mes, dia = evaluar_fecha(anio, mes, dia, registro_encontrado)
                else:
                    registro_encontrado = False    
                    anio, mes, dia = evaluar_fecha(anio, mes, dia, registro_encontrado)

    if decision_usuario == 2:

        numero_pais_a_consultar = None
        pais, anio, mes, dia = ingreso_de_datos_a_consultar(decision_usuario, numero_pais_a_consultar)
        imprimir_data_pais(data_vacunacion, pais, anio, mes, dia, decision_usuario)
    
    if decision_usuario == 3:

        numero_pais_a_consultar = 1
        pais_uno, anio, mes, dia = ingreso_de_datos_a_consultar(decision_usuario, numero_pais_a_consultar)
        numero_pais_a_consultar = 2
        pais_dos, anio, mes, dia = ingreso_de_datos_a_consultar(decision_usuario, numero_pais_a_consultar)
        imprimir_data_pais(data_vacunacion, pais_uno, anio, mes, dia, decision_usuario)
        imprimir_data_pais(data_vacunacion, pais_dos, anio, mes, dia, decision_usuario)


def main():
    # se abre archivo json que contiene informacion solicitdada de acuerdo al proceso de vacunacion en cada pais registrado
    data_vacunacion = abrir_archivo_json()
    # se dirigue a funcion 'menu', la cual corresponde al menu inicial en donde usuario decide item por el cual consultar
    decision_usuario = menu()
    # se evalua la decision de usuario, tal que programa ejecutara las lineas dependientes de la decision de usuario
    procesar_decision_usuario(decision_usuario, data_vacunacion)

if __name__ == "__main__":
    main()
