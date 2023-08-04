import funciones

url = 'https://api.worldbank.org/v2/country/{id}{indicator}?per_page={resul}{date}&format=json'


ids,names,idsYnames = funciones.listar_paisesXprimera_vez(url)# solo hace falta llamar al API una vez ya que los valores permanecen guardados en las variables que recibieron la respuesta
print("En este programa podrá ver algunos datos acerca de un país en específico\nAcontinuación se le presentará un listado con los países diponibles,  presione ENTER para continuar")
input()


while True:    
    print("ID ", "Nombre completo") # titulos de las columnas
    for i in idsYnames: # lista id y nombre de cada país en pares individuales para más legibilidad
        print(i,idsYnames[i])
    
    while True: #para validar que el id digitado sea correcto
        dato = input("Digite el ID del país a consultar:   ").upper()
        if dato in ids:
            break
        else: print("                                           !  El valor digitado no es un ID válido  !")

    print("Seleccione que consulta desea realizar:\n", "1. Poblacion general   ", "2. Poblacion femenina   ", "3. Poblacion masculina\n","4. Capital   " )
    seleccion = input()
    
    match seleccion:
        case '1':
            #**********     poblacion general
            #proximamente selección de fechas....
            # fecha = input("Puede seleccionar un año específico o un rango de años de la forma (2010:2020) de lo contrario se mostrará la información de los últimos 50 años   ")
            poblacion = funciones.poblacion(url,dato,fecha='2000:2023')#si se quiere elegir un año específico  o un rango se usa: 2010:2022'
            for anno in poblacion:
                print(f"Para el año {anno['date']} se registró un total de {anno['value']} personas")
            #**********     poblacion general

        case '2':
            #**********     Mujeres
            poblacionF = funciones.poblacion_femenina(url,dato,fecha='2000:2023')#si se quiere elegir un año específico  o un rango se usa: 2010:2022'
            for anno in poblacionF:
                print(f"Para el año {anno['date']} se registró un total de {anno['value']} mujeres")
            #**********     Mujeres

        case '3':
            #**********     Hombres
            poblacionM = funciones.poblacion_masculina(url,dato,fecha='2000:2023')#si se quiere elegir un año específico  o un rango se usa: 2010:2022'
            for anno in poblacionM:
                print(f"Para el año {anno['date']} se registró un total de {anno['value']} hombres")
            #**********     Hombres
        case '4':
            # ---------     capitales
            pais, capital = funciones.capitalEs(url,dato)
            print(f"La capital de {pais} es {capital}")
            # ---------     capitales
        case _:
            print(seleccion,"no es una opción válida")
    
    salir = input("¿Desea realizar otra consulta?   S/N").upper()
    if salir == 'N':
        break
    

    


#↓↓↓ ↓↓↓ ↓↓↓   ignorar   ↓↓↓ ↓↓↓ ↓↓↓
"""
otros indicadores
SP.RUR.TOTL = rural population
SP.POP.GROW = annual% population grow
"""
#responseAnalisis = [{'page': 1, 'pages': 1, 'per_page': '50', 'total': 1}, [{'id': 'CRI', 'iso2Code': 'CR', 'name': 'Costa Rica', 'region': {'id': 'LCN', 'iso2code': 'ZJ', 'value': 'Latin America & Caribbean '}, 'adminregion': {'id': 'LAC', 'iso2code': 'XJ', 'value': 'Latin America & Caribbean (excluding high income)'}, 'incomeLevel': {'id': 'UMC', 'iso2code': 'XT', 'value': 'Upper middle income'}, 'lendingType': {'id': 'IBD', 'iso2code': 'XF', 'value': 'IBRD'}, 'capitalCity': 'San Jose', 'longitude': '-84.0089', 'latitude': '9.63701'}]]