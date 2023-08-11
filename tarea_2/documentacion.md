# Tarea #1 python intermedio
## Consumo de  datos de una API
#### Introducción  

La API utilizada fue "The World Bank", la documentación completa se encuentra [aquí](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information).  
Se utilizan principalmente datos acerca de la población de los **297 países disponibles** en la base de datos, específicamente datos sobre población general, cantidad de hombres y mujeres y la capital, se planea integrar también información acerca del crecimiento anual de la población, porcentaje de poblacion rural entre otros.

Se eligío esta API por la naturaleza de los datos que se pueden extraer además de que es relativamente sencillo solicitar información especial porque ya integra diferentes endpoints para cada consulta específica, también permite previzualizar los resultados en el navagador en formato XML y con una pequeña modificación a la url del endpoint se pueden solicitar los datos en formato JSON además de que no requiere una APIkey o autentificación como se menciona en la documentación.
>API Access / Authentication
>>API keys and other authentication methods are no longer necessary to access the API.

#### Endpoints
Los endpoint que se utilizaron usan un método de consulta basado en argumentos.  
Tal vez un buen punto de partida sea la siguiente url:  
###### https://api.worldbank.org/v2/country/all
Aquí se pueden ver, en forma XML, datos generales de todos los países en la base de datos como el nombre, la abreviación, la capital, latitud, longitud y la región a la que pertenecen. Se pueden agregar un par de argumentos para modificar como se muestran los resultados por ejemplo:
###### https://api.worldbank.org/v2/country/all?per_page=100&page=2
Con estos agregados se obtienen páginas con 100 resultados cada una y muestra los datos de la página 2, así se puede controlar cuantos datos se obtienen en cada consulta a la API, también si al final se agrega *"&format=json"* la respuesta estará en formato JSON en lugar de XML.

Ejemplo de respuesta:

XML
><wb:countries xmlns:wb="http://www.worldbank.org" page="1" pages="1"   per_page="50" total="1">  
<wb:country id="CRI">  
<wb:iso2Code>CR</wb:iso2Code>  
<wb:name>Costa Rica</wb:name>  
<wb:region id="LCN" iso2code="ZJ">Latin America & Caribbean </wb:region>  
<wb:adminregion id="LAC" iso2code="XJ">Latin America & Caribbean (excluding high income)</wb:adminregion>  
<wb:incomeLevel id="UMC" iso2code="XT">Upper middle income</wb:incomeLevel>  
<wb:lendingType id="IBD" iso2code="XF">IBRD</wb:lendingType>  
<wb:capitalCity>San Jose</wb:capitalCity>  
<wb:longitude>-84.0089</wb:longitude>  
<wb:latitude>9.63701</wb:latitude>  
</wb:country>  
</wb:countries>  

JSON

>[{  
>   "page":1,"pages":1,"per_page":"50","total":1  
},  
[{  
"id":"CRI","iso2Code":"CR","name":"Costa Rica",  
"region":{"id":"LCN","iso2code":"ZJ","value":"Latin America & Caribbean "},
  "adminregion":{"id":"LAC","iso2code":"XJ","value":"Latin America & Caribbean (excluding high income)"},  
  "incomeLevel":{"id":"UMC","iso2code":"XT","value":"Upper middle income"},  
  "lendingType":{"id":"IBD","iso2code":"XF","value":"IBRD"},"capitalCity":"San Jose","longitude":"-84.0089","latitude":"9.63701"  
}]]

Para seleccionar un país particular solo hace falta sustituir *"all"* por el **id** del país de interés que se puede encontrar en cualquiera de las direcciones anteriores, por ejemplo *"CRI"* para Costa Rica.

Ahora, para solicitar información específica la API usa lo que llama *"indicators"* que apuntan a datos determinados sobre desarrollo social, económico o educativo, entre otros. Cada indicador tiene una codificación que se puede encontrar en [este enlace](http://api.worldbank.org/v2/indicator) con más de 20 mil opciones pero no todas aplican a todos los países.

Los indicadores que se han usado **hasta el momento** en este programa son:
* SP.POP.TOTL =>para el total de población
* SP.POP.TOTL.FE.IN =>total femenino
* SP.POP.TOTL.MA.IN  =>total masculino  

Y un ejemplo de la manera en la que se implemetaron en el código es:  
```https://api.worldbank.org/v2/country/{país}/indicator/{código}&format=json```  
Donde *"país"* corresponde al ID del país de interés y *"código"* a la codificación que haya asignado la API al indicador que se busca.

Otros indicadores que se pretenden implementar son:
* SP.RUR.TOTL = rural population
* SP.POP.GROW = annual% population grow  

Así como también selección de rangos de fechas y posiblemente otra categoria de indicadores.

Hasta aquí la primera parte.

----------------------------------------------------------------------------
# Tarea #2 python intermedio

En esta segunda parte se agregaron más indicadores para consultas, por tanto un menú más amplio y mejoras a pequeños detalles así como también las gráficas que son el enfasis de la nueva rúbrica.

Los "indicators" agregados fueron:
- [x] Población rural
- [x] Población urbana
- [x] % crecimiento anual
- [x] Fuerza laboral total
- [x] Fuerza laboral en agricultura
- [x] Fuerza laboral autoempleda
- [x] Personas mayores a 65 años
- [x] % de mujeres que sobrevive hasta los 65 años
- [x] % de hombres que sobrevive hasta los 65 años

También en esta parte se agregó la posibilidad de elegir un año o rango de años para los que se quiere solicitar la información. Además, si el rango de años elegido es igual o mayor a 10 la consola le presentará la opción de ver  <mark>un gráfico simple</mark> sobre los datos seleccionados, esto para todos y cada uno de los indicadores expuestos arriba.

En el tema de gráficos, las visualizaciones elegidas fueron las siguientes:

<img src="bar_plot.PNG" width="200" height="200"> <img src="stem_plot.PNG" width="200" height="200"> <img src="nested_pie.PNG" width="200" height="200">

Se eligieron estos gráficos porque se considera que pueden reprensentar de manera ilustrativa los datos elegidos para este trabajo por ejemplo: para los resultados de los "indicators" se usó el gráfico de en medio porque permite visualizar los cambios a lo largo del tiempo ya que todos estos datos se toman por año.

El <mark>gráfico de barras</mark> se usó en un top 10 de países con mayor población, de esta manera considero que es más impactante hacer esta comparación ya que permite ver de manera proporcional los cambios.

Finalmente el <mark>grafico de pie</mark> se usó para visualizar datos acerca de las proporciones de hombres y mujeres así como también el porcentaje de cada uno que logra sobrevivir hasta los 65 años 