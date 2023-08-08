import pandas
import matplotlib.pyplot as matplot

data = pandas.read_csv("ventas.csv") # importa el archivo como dataFrame
ganancia = data.loc[:,'Ventas']-data.loc[:,'Gastos'] # saca la diferencia de los valores en las columnas ventas y gastos
data['Ganancia'] = ganancia # Crea una nueva columna en el dataFrame y le asigna los valores que se calcularon

# ▼▼▼   para referencia futura, ignorar este bloque para la revisión, me equivoqué de gráfico... ▼▼▼
#                                    ▼
# posX = [x for x in range(1,13)] # listas para setear las posiciones del eje x para las barras
# posX2=[i-0.5 for i in range(1,13)] # y evitar que queden superpuestas
# matplot.bar(posX,data.loc[:,'Ventas'].values,width=0.35,label='Ventas',color='navy') #setea la primera barra, posición, magnitudes, atributos/parámetros
# matplot.bar(posX2,data.loc[:,'Gastos'].values,width=0.35,align='edge',label="Gastos",color="darkred") # setea la segunda variable
# matplot.xticks(posX,data.loc[:,'Mes'].values,rotation=45) # asigna posición, valor y ajustes a las etiquetas del eje x
# matplot.legend(loc ="upper left") # setea la posición de las legendas
#                                   ▲

matplot.plot(data.loc[:,'Mes'].values,data.loc[:,'Ventas'].values,label='Ventas',color='navy')#setea la primera línea, magnitudes y atributos
matplot.plot(data.loc[:,'Mes'].values,data.loc[:,'Gastos'].values,label='Gastos',color="darkred")#setea la segunda línea
matplot.xticks(rotation=45) # ajusta las etiquetas del eje x para que sean más legibles
matplot.legend(loc ="upper left") # setea la posición de las legendas

matplot.title("Comparativa anual de gastos contra ventas")
matplot.xlabel("MES")
matplot.ylabel("Cantidad")
matplot.show()


