import funciones
import matplotlib.pyplot as matplot

#                   Índice
#Capitales     ------------------ case '1' | línea 54
#Población total ---------------- case '2' | línea 58
#Población femenina ------------- case '3' | línea 87
#Población masculina ------------ case '4' | línea 116
#Población rural ---------------- case '5' | línea 145
#Población urbana --------------- case '6' | línea 175
#% crecimiento anual ------------ case '7' | línea 204
#Total de personas empledas ----- case '8' | línea 232
#% de empleados en agricultura -- case '9' | línea 261
#% empleados independientes ----- case '10'| línea 289
#Personas mayores a 65 años ----- case '11'| línea 317
#Mujeres hasta 65 años ---------- case '12'| línea 346
#Hombres hasta 65 años ---------- case '13'| línea 374
#Gráfica proporción H/M +65 ----- case '14'| línea 402
#Gráfica mayor población -------- case '15'| línea 426

url = 'https://api.worldbank.org/v2/country/{id}{indicator}?per_page={resul}{date}&format=json'

rango_annos = [i for i in range(1963,2023)]# para guardar y comparar los años que acepta la API
ids,names,idsYnames = funciones.listar_paisesXprimera_vez(url)# solo hace falta llamar al API una vez ya que los valores permanecen guardados en las variables que recibieron la respuesta
print("En este programa podrá ver algunos datos acerca de un país en específico\n")

while True:    # bucle principal del programa
    #primer menú
    print("\nSeleccione que consulta desea realizar digitando el número correspondiente:\n", "1. Capital   ","2. Poblacion general   ", "3. Poblacion femenina   ", "4. Poblacion masculina   ","5. Población rural   ","6. Población urbana\n",
          "\n7. Porcentaje de crecimiento anual   ","8. Total de personas empleadas   ","9. Porcentaje de empleados en agricultura\n",
          "\n10. Porcentaje de empleados independientes   ","11. Personas mayores a 65 años   ","12. Mujeres hasta 65 años   ", "13. Hombres hasta 65 años\n",
          "\n14. Gráfica sobre la proporción de hombres y mujeres para el año 2021 ","    15. Top 10 paises con mayor población")
    seleccion = input()
    
    if seleccion in [str(i) for i in range(1,15)]:
        print("Acontinuación se le presentará un listado con los países diponibles,  presione ENTER para continuar")
        input()
        
        print("ID |", "Nombre completo\n","--|--------------") # títulos de las columnas
        for i in idsYnames: # lista los id y nombre de cada país en pares individuales para más legibilidad
            print(i,idsYnames[i])
        
        while True: #para validar que el id digitado sea correcto
            pais = input("Digite el ID del país a consultar:   ").upper()
            if pais in ids:
                break
            else: print("                                           !  El valor digitado no es un ID válido  !")    

    #  ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲  

    match seleccion:
        case '1':# •••••    capitales 
            pais, capital = funciones.capitalEs(url,pais)
            print(f"La capital de {pais} es {capital}")    
#♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ 
        case '2':# •••••    poblacion general/total 
            desde, hasta = funciones.toma_de_fechas() # funcion para validar y verificar que el número se encuentre entre en rango disponible por la API
            poblacion = funciones.poblacion(url,pais,fecha=f'{desde}:{hasta}')
            poblacionTot = []#para registrar todos los valores y posteriormente graficarlos
            rango_graf_annos = [] # Para registar el rango de años elegidos para enparejar en la gráfica
            for anno in poblacion:
                if anno['value'] == None:#para evitar que se caiga si la base de datos no tiene infomarción para los años especificados 
                    print(f"No hay datos para el año {anno['date']}")
                    poblacionTot.append(0)
                    rango_graf_annos.append(anno['date'])#registra el año para poder graficar luego
                else:
                    print(f"Para el año {anno['date']} se registró un total de {anno['value']:,} personas")
                    poblacionTot.append(anno['value']) # registra el valor de la iteración actual
                    rango_graf_annos.append(anno['date'])
            # gráfica simple
            grafica = input("¿Desea ver una gráfica simple?   S/N").upper()
            if len(rango_graf_annos) >= 10:
                if grafica == 'S':
                    poblacionTot.reverse()#invierte el orden de los valores de la lista porque en la respuesta de la API se recibieron de mayor a menor                        
                    rango_graf_annos.reverse()
                    matplot.stem(rango_graf_annos,poblacionTot)
                    matplot.ticklabel_format(style='sci', axis='y',scilimits=(6,6))
                    matplot.title(f"Cambio de la población en {idsYnames[pais]}")
                    matplot.xlabel("Año")
                    matplot.ylabel("Millones")
                    matplot.xticks(rotation=90)
                    matplot.grid(axis='y')
                    matplot.show()
#♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ 
        case '3':# •••••    Mujeres
            desde, hasta = funciones.toma_de_fechas()
            poblacionF = funciones.poblacion_femenina(url,pais,fecha=f'{desde}:{hasta}')
            mujeres = []
            rango_graf_annos = [] # Para registar el rango de años elegidos para enparejar en la gráfica
            for anno in poblacionF:
                if anno['value'] == None:#para evitar que se caiga si la base de datos no tiene infomarción para los años especificados 
                    print(f"No hay datos para el año {anno['date']}")
                    mujeres.append(0)
                    rango_graf_annos.append(anno['date'])#registra el año para poder graficar luego
                else:
                    print(f"Para el año {anno['date']} se registró un total de {anno['value']:,} mujeres")
                    mujeres.append(anno['value'])
                    rango_graf_annos.append(anno['date'])
            # gráfica simple
            if len(rango_graf_annos) >= 10:
                grafica = input("¿Desea ver una gráfica simple?   S/N").upper()
                if grafica == 'S':
                    mujeres.reverse()
                    rango_graf_annos.reverse()
                    matplot.stem(rango_graf_annos,mujeres)
                    matplot.ticklabel_format(style='sci', axis='y',scilimits=(6,6))
                    matplot.title(f"Total de mujeres por año en {idsYnames[pais]}")
                    matplot.xlabel("Año")
                    matplot.ylabel("Millones")
                    matplot.xticks(rotation=90)
                    matplot.grid(axis='y')
                    matplot.show()
#♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ 
        case '4':# •••••    Hombres
            desde, hasta = funciones.toma_de_fechas()
            poblacionM = funciones.poblacion_masculina(url,pais,fecha=f'{desde}:{hasta}')#solicita los datos
            hombres = []# para registrar las magnitudes individualmente
            rango_graf_annos = [] # Para registar el rango de años elegidos para enparejar en la gráfica
            for anno in poblacionM:
                if anno['value'] == None:#para evitar que se caiga si la base de datos no tiene infomarción para los años especificados 
                    print(f"No hay datos para el año {anno['date']}")
                    hombres.append(0)#agrega un 0 a lista para que se mantenga con la misma longitud que los años para la hora de graficar
                    rango_graf_annos.append(anno['date'])#registra el año para poder graficar luego
                else:
                    print(f"Para el año {anno['date']} se registró un total de {anno['value']:,} hombres")
                    hombres.append(anno['value'])
                    rango_graf_annos.append(anno['date'])
            # gráfica simple
            if len(rango_graf_annos) >= 10:
                grafica = input("¿Desea ver una gráfica simple?   S/N").upper()
                if grafica == 'S':
                    hombres.reverse()
                    rango_graf_annos.reverse()
                    matplot.stem(rango_graf_annos,hombres)
                    matplot.ticklabel_format(style='sci', axis='y',scilimits=(6,6))
                    matplot.title(f"Total de hombres por año en {idsYnames[pais]}")
                    matplot.xlabel("Año")
                    matplot.ylabel("Millones")
                    matplot.xticks(rotation=90)
                    matplot.grid(axis='y')
                    matplot.show()
#♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ 
        case '5':# •••••    población rural
            desde, hasta = funciones.toma_de_fechas()
            poblacionRu = funciones.poblacion_rural(url,pais,fecha=f'{desde}:{hasta}')
            rurales = []
            rango_graf_annos = [] 
            for anno in poblacionRu:
                if anno['value'] == None:#para evitar que se caiga si la base de datos no tiene infomarción para los años especificados 
                    print(f"No hay datos para el año {anno['date']}")
                    rurales.append(0)
                    rango_graf_annos.append(anno['date'])#registra el año para poder graficar luego
                else:
                    print(f"Para el año {anno['date']} se registró un total de {anno['value']:,} personas en áreas rurales")
                    rurales.append(anno['value'])
                    rango_graf_annos.append(anno['date'])
            # gráfica simple
            grafica = input("¿Desea ver una gráfica simple?   S/N").upper()
            if len(rango_graf_annos) >= 10:
                if grafica == 'S':
                    rurales.reverse()
                    rango_graf_annos.reverse()
                    rango_graf_annos.reverse()
                    matplot.stem(rango_graf_annos,rurales)
                    matplot.ticklabel_format(style='sci', axis='y',scilimits=(6,6))
                    matplot.title(f"Total de personas en áreas rurales por año en {idsYnames[pais]}")
                    matplot.xlabel("Año")
                    matplot.ylabel("Millones")
                    matplot.xticks(rotation=90)
                    matplot.grid(axis='y')
                    matplot.show()
#♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ 
        case '6':# •••••    población urbana
            desde, hasta = funciones.toma_de_fechas()
            poblacionUrb = funciones.poblacion_urbana(url,pais,fecha=f'{desde}:{hasta}')
            urbanos = []
            rango_graf_annos = [] 
            for anno in poblacionUrb:
                if anno['value'] == None:#para evitar que se caiga si la base de datos no tiene infomarción para los años especificados 
                    print(f"No hay datos para el año {anno['date']}")
                    urbanos.append(0)
                    rango_graf_annos.append(anno['date'])
                else:
                    print(f"Para el año {anno['date']} se registró un total de {anno['value']:,} personas en áreas urbanas")
                    urbanos.append(anno['value'])
                    rango_graf_annos.append(anno['date'])
            # gráfica simple
            grafica = input("¿Desea ver una gráfica simple?   S/N").upper()
            if len(rango_graf_annos) >= 10:
                if grafica == 'S':
                    urbanos.reverse()
                    rango_graf_annos.reverse()
                    matplot.stem(rango_graf_annos,urbanos)
                    matplot.ticklabel_format(style='sci', axis='y',scilimits=(6,6))
                    matplot.title(f"Total de personas en áreas urbanas por año en {idsYnames[pais]}")
                    matplot.xlabel("Año")
                    matplot.ylabel("Millones")
                    matplot.xticks(rotation=90)
                    matplot.grid(axis='y')
                    matplot.show()
#♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ 
        case '7':# •••••    % de crecimiento anual
            desde, hasta = funciones.toma_de_fechas()
            crecimiento = funciones.crecimiento_anual(url,pais,fecha=f'{desde}:{hasta}')
            porc_anual = []
            rango_graf_annos = [] 
            for anno in crecimiento:
                if anno['value'] == None:#para evitar que se caiga si la base de datos no tiene infomarción para los años especificados 
                    print(f"No hay datos para el año {anno['date']}")
                    porc_anual.append(0)
                    rango_graf_annos.append(anno['date'])
                else:
                    print(f"Para el año {anno['date']} se registró un {anno['value']:.2f} porciento de crecimiento en la población")
                    porc_anual.append(anno['value'])
                    rango_graf_annos.append(anno['date'])
            # gráfica simple
            grafica = input("¿Desea ver una gráfica simple?   S/N").upper()
            if len(rango_graf_annos) >= 10:
                if grafica == 'S':
                    porc_anual.reverse()
                    rango_graf_annos.reverse()
                    matplot.stem(rango_graf_annos,porc_anual)
                    matplot.title(f"Porcentaje de crecimiento poblacional anual en {idsYnames[pais]}")
                    matplot.xlabel("Año")
                    matplot.ylabel("Porcentaje")
                    matplot.xticks(rotation=90)
                    matplot.grid(axis='y')
                    matplot.show()
#♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ 
        case '8':# •••••    total de personas empleadas
            desde, hasta = funciones.toma_de_fechas()
            total_empleados = funciones.Flaboral_total(url,pais,fecha=f'{desde}:{hasta}')
            empleados = []
            rango_graf_annos = [] 
            for anno in total_empleados:
                if anno['value'] == None:#para evitar que se caiga si la base de datos no tiene infomarción para los años especificados 
                    print(f"No hay datos para el año {anno['date']}")
                    empleados.append(0)
                    rango_graf_annos.append(anno['date'])
                else:
                    print(f"Para el año {anno['date']} se registró un total de {anno['value']:,} personas trabajando")
                    empleados.append(anno['value'])
                    rango_graf_annos.append(anno['date'])                    
            # gráfica simple
            grafica = input("¿Desea ver una gráfica simple?   S/N").upper()
            if len(rango_graf_annos) >= 10:
                if grafica == 'S':
                    empleados.reverse()
                    rango_graf_annos.reverse()
                    matplot.stem(rango_graf_annos,empleados)
                    matplot.ticklabel_format(style='sci', axis='y',scilimits=(6,6))
                    matplot.title(f"Total de personas empleadas por año en {idsYnames[pais]}")
                    matplot.xlabel("Año")
                    matplot.ylabel("Millones")
                    matplot.xticks(rotation=90)
                    matplot.grid(axis='y')
                    matplot.show()            
#♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ 
        case '9':# •••••    % de empleados en área agricultura
            desde, hasta = funciones.toma_de_fechas()
            agriempleados = funciones.Flaboral_agricultura(url,pais,fecha=f'{desde}:{hasta}')
            porc_agri = []
            rango_graf_annos = [] 
            for anno in agriempleados:
                if anno['value'] == None:#para evitar que se caiga si la base de datos no tiene infomarción para los años especificados 
                    print(f"No hay datos para el año {anno['date']}")
                    porc_agri.append(0)
                    rango_graf_annos.append(anno['date'])
                else:
                    print(f"Para el año {anno['date']} se registró un {anno['value']:.2f} porciento del total de empledos trabajando en áreas de agricultura")
                    porc_agri.append(anno['value'])
                    rango_graf_annos.append(anno['date'])
            # gráfica simple
            grafica = input("¿Desea ver una gráfica simple?   S/N").upper()
            if len(rango_graf_annos) >= 10:
                if grafica == 'S':
                    porc_agri.reverse()
                    rango_graf_annos.reverse()
                    matplot.stem(rango_graf_annos,porc_agri)
                    matplot.title(f"Porcentaje de los empleados laborando en el área de agricultura por año en {idsYnames[pais]}")
                    matplot.xlabel("Año")
                    matplot.ylabel("Porcentaje")
                    matplot.xticks(rotation=90)
                    matplot.grid(axis='y')
                    matplot.show()
#♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ 
        case '10':# •••••    % de empleados independientes
            desde, hasta = funciones.toma_de_fechas()
            autoempleados = funciones.Flaboral_autoempleda(url,pais,fecha=f'{desde}:{hasta}')
            indEmpleados = []
            rango_graf_annos = [] 
            for anno in autoempleados:
                if anno['value'] == None:#para evitar que se caiga si la base de datos no tiene infomarción para los años especificados 
                    print(f"No hay datos para el año {anno['date']}")
                    indEmpleados.append(0)
                    rango_graf_annos.append(anno['date'])
                else:
                    print(f"Para el año {anno['date']} se registró un {anno['value']:.2f} porciento del total de empledos trabajando de forma independiente")
                    indEmpleados.append(anno['value'])
                    rango_graf_annos.append(anno['date'])
            # gráfica simple
            grafica = input("¿Desea ver una gráfica simple?   S/N").upper()
            if len(rango_graf_annos) >= 10:
                if grafica == 'S':
                    indEmpleados.reverse()
                    rango_graf_annos.reverse()
                    matplot.stem(rango_graf_annos,indEmpleados)
                    matplot.title(f"Porcentaje de empleados laborando independientemente por año en {idsYnames[pais]}")
                    matplot.xlabel("Año")
                    matplot.ylabel("Porcentaje")
                    matplot.xticks(rotation=90)
                    matplot.grid(axis='y')
                    matplot.show()
#♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ 
        case '11':# •••••    población mayor a 65 años
            desde, hasta = funciones.toma_de_fechas()
            mayores65 = funciones.mayores65(url,pais,fecha=f'{desde}:{hasta}')
            mas65graf = []
            rango_graf_annos = [] 
            for anno in mayores65:
                if anno['value'] == None:#para evitar que se caiga si la base de datos no tiene infomarción para los años especificados 
                    print(f"No hay datos para el año {anno['date']}")
                    mas65graf.append(0)
                    rango_graf_annos.append(anno['date'])
                else:
                    print(f"Para el año {anno['date']} se registró un total de {anno['value']:,} personas mayores a los 65 años")
                    mas65graf.append(anno['value'])
                    rango_graf_annos.append(anno['date'])
            # gráfica simple
            grafica = input("¿Desea ver una gráfica simple?   S/N").upper()
            if len(rango_graf_annos) >= 10:
                if grafica == 'S':
                    mas65graf.reverse()
                    rango_graf_annos.reverse()
                    matplot.stem(rango_graf_annos,mas65graf)
                    matplot.ticklabel_format(style='sci', axis='y',scilimits=(6,6))
                    matplot.title(f"Total de personas mayores a 65 años en {idsYnames[pais]}")
                    matplot.xlabel("Año")
                    matplot.ylabel("Millones")
                    matplot.xticks(rotation=90)
                    matplot.grid(axis='y')
                    matplot.show()
#♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ 
        case '12':# •••••    % de mujeres que llega a los 65
            desde, hasta = funciones.toma_de_fechas()
            mujeres65 = funciones.mujeres_hasta65(url,pais,fecha=f'{desde}:{hasta}')
            muj_Hasta65= []
            rango_graf_annos = [] 
            for anno in mujeres65:
                if anno['value'] == None:#para evitar que se caiga si la base de datos no tiene infomarción para los años especificados 
                    print(f"No hay datos para el año {anno['date']}")
                    muj_Hasta65.append(0)
                    rango_graf_annos.append(anno['date'])
                else:
                    print(f"Para el año {anno['date']} se registró un {anno['value']:.2f} porciento del total de mujeres que se encuentran sobre los 65 años")
                    muj_Hasta65.append(anno['value'])
                    rango_graf_annos.append(anno['date'])
            # gráfica simple
            grafica = input("¿Desea ver una gráfica simple?   S/N").upper()
            if len(rango_graf_annos) >= 10:
                if grafica == 'S':
                    muj_Hasta65.reverse()
                    rango_graf_annos.reverse()
                    matplot.stem(rango_graf_annos,muj_Hasta65)
                    matplot.title(f"Porcentaje del total de mujeres que sobreviven hasta los 65 años en {idsYnames[pais]}")
                    matplot.xlabel("Año")
                    matplot.ylabel("Porcentaje")
                    matplot.xticks(rotation=90)
                    matplot.grid(axis='y')
                    matplot.show()
#♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ 
        case '13':# •••••    % de hombres que llega a los 65
            desde, hasta = funciones.toma_de_fechas()
            hombres65 = funciones.hombres_hasta65(url,pais,fecha=f'{desde}:{hasta}')
            hom_Hasta65 = []
            rango_graf_annos = [] 
            for anno in hombres65:
                if anno['value'] == None:#para evitar que se caiga si la base de datos no tiene infomarción para los años especificados 
                    print(f"No hay datos para el año {anno['date']}")
                    hom_Hasta65.append(0)
                    rango_graf_annos.append(anno['date'])
                else:
                    print(f"Para el año {anno['date']} se registró un {anno['value']:.2f} porciento del total de hombres que se encuentran sobre los 65 años")
                    hom_Hasta65.append(anno['value'])
                    rango_graf_annos.append(anno['date'])
            # gráfica simple
            grafica = input("¿Desea ver una gráfica simple?   S/N").upper()
            if len(rango_graf_annos) >= 10:
                if grafica == 'S':
                    hom_Hasta65.reverse()
                    rango_graf_annos.reverse()
                    matplot.stem(rango_graf_annos,hom_Hasta65)
                    matplot.title(f"Porcentaje del total de hombres que sobreviven hasta los 65 años en {idsYnames[pais]}")
                    matplot.xlabel("Año")
                    matplot.ylabel("Porcentaje")
                    matplot.xticks(rotation=90)
                    matplot.grid(axis='y')
                    matplot.show()
#♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ 
        case '14': #•••••       gráficas       
            hombres = funciones.poblacion_masculina(url,pais,fecha="2021")#solicita el dato a la API
            mujeres = funciones.poblacion_femenina(url,pais,fecha="2021")
            hom_Hasta65 = funciones.hombres_hasta65(url,pais,fecha="2021")
            muj_Hasta65 = funciones.mujeres_hasta65(url,pais,fecha="2021")
            nivel1 = [hombres[0]['value'],mujeres[0]['value']] #se juntan los datos internos y externos del pie en listas aparte para facilitar lectura y ejecución del gráfico
            nivel2 = [hom_Hasta65[0]['value'],100-hom_Hasta65[0]['value'],muj_Hasta65[0]['value'],100-muj_Hasta65[0]['value']]

            fig, ax = matplot.subplots()# se crea el objeto gráfico y eje
            size = 0.3 # se setea el tamaño de los niveles
            cmap = matplot.colormaps["tab20c"] # setea las categorias de colores
            outer_colors = cmap([0,4,8]) # se setean los respectivos colores para cada nivel
            inner_colors = cmap([1, 2, 5, 6, 9, 10])

            ax.pie(nivel1, radius=1, colors=outer_colors,labels=[f'{i:,}' for i in nivel1],labeldistance=0.8, # datos y propiedades del primer nivel
                wedgeprops=dict(width=size, edgecolor='w'))

            ax.pie(nivel2, radius=1-size, colors=inner_colors,labels=[f'{i:.2f}%' for i in nivel2],labeldistance=0.7,# datos y propiedades del segundo nivel
                wedgeprops=dict(width=size, edgecolor='w'))
            
            ax.set( title=f'Proporcion de hombres y mujeres\n Porcentaje de supervivencia hasta los 65 años\n en {idsYnames[pais]} para el 2021')
            matplot.legend(loc=(-0.4, -0.1),labels=["Total de hombres","Total de mujeres","% de hombres que llega a los 65 años","% de hombres que fallece antes de los 65","% de mujeres que llega a los 65 años","% de mujeres que fallece antes de los 65"])
            matplot.show()
#♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ 
        case '15': 
    #Top 10 paises con mayor población → india, china, US, pakistan, nigeria, brazil, bangladesh, russia, mexico, ethiopia
            paises = {"India":"IND", "China":"CHN","Usa":"USA","Pakistan":"PAK","Nigeria":"NGA","Brazil":"BRA","Bangladesh":"BGD","Russia":"RUS","Mexico":"MEX","Ethiopia":"ETH"} #listado de países con mayor población
            for pais in paises:
                gente = funciones.poblacion(url,paises[pais],"2022")#solicita a la API el valor para cada país
                matplot.bar(pais,gente[0]['value'])#crea una barra para cada país y le asigna el valor obtenido
                print("       •")# para ilustrar en consola que algo esta pasando ya que los calls a la API pueden tomar algo de tiempo
            matplot.ticklabel_format(style='sci', axis='y',scilimits=(6,6))#modifica los números del eje y, en estilo científico para no ocupar demasiado espacio y limita la notación para que esté en magnitud de millones
            matplot.xticks(range(0,10),paises.keys(),rotation=30)#setea las pocisiones de las barras en el eje x, las etiquetas para cada una y una rotacion de 30 grados
            matplot.title("Los 10 países con mayor población en el mundo para el 2022")
            matplot.ylabel("Millones")
            matplot.show()
#♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ 
        case _:# case default
            print(" la consulta selecionada no es una opción válida")
    
    salir = input("¿Desea realizar otra consulta?   S/N").upper()
    if salir == 'N':
        break
    

    


#↓↓↓ ↓↓↓ ↓↓↓   ignorar   ↓↓↓ ↓↓↓ ↓↓↓
"""
otros indicadores
SP.RUR.TOTL = rural population
SP.URB.TOTL = urban population
SP.POP.GROW = annual% population grow
EN.URB.LCTY = Population in largest city
SL.TLF.TOTL.IN = Labor force, total
SL.AGR.EMPL.ZS = labor force in agriculture
SP.POP.65UP.TO = population at 65+ years old
SH.STA.TRAF.P5 = Mortality caused by road traffic injury (per 100,000 population)
SP.DYN.TO65.FE.ZS = Survival to age 65, female
SL.EMP.SELF.ZS = Self-employed, total (% of total employment)
"""
#responseAnalisis = [{'indicator': {'id': 'SP.POP.TOTL', 'value': 'Population, total'}, 'country': {'id': 'ET', 'value': 'Ethiopia'}, 'countryiso3code': 'ETH', 'date': '2022', 'value': 123379924, 'unit': '', 'obs_status': '', 'decimal': 0}]