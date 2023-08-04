import requests
# API documentation url = https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information


apiUrl = 'http://api.worldbank.org/v2'
#uurl = 'https://api.worldbank.org/v2/country/all?per_page=100&format=json'
#para que la respuesta sea en formato json se debe agregar el argumento "?format=json" o "&format=json" para cuando se usa más de un argumento
#el argumento "per_page=100" se puede modificar para escoger cuantos resultados se reciben en la respuesta y evitar saturación de información
#country/all/indicator/SP.POP.TOTL => para solicitar el total de población, se puede agregar fecha ?date=2000


url_para_pruebas = 'https://api.worldbank.org/v2/country/{id}{indicator}?per_page={resul}{date}&format=json'
ids = [] #para listar los IDs que acepta la API
names = [] #para listar los nombres completos de cada ID
idsYnames = {} #para juntar cada ID con su nombre respectivo


def dar_formato(url,id='all',resul=60,indicator="",date=""):#para dar formato a la url y llegar al endpoint buscado, se crea en una función aparte para no tener que setear siempre todos los valores, solo lo que se necesite en el momento
    new_url = url.format(id=id,resul=resul,indicator=indicator,date=date)#asigna los valores correspondientes o deja los que se asignaron por defecto
    return new_url #devuelve la url ajustada


def listar_paisesXprimera_vez(url):#para obtener los diminutivos y nombres completos de cada país
    response = requests.get(dar_formato(url,resul=300)) #se ejecuta la consulta a la API y se definen los valores necesarios en la url
    result = response.json()
    for i in result[1]: #se usa el segundo índice porque es el que trae la información como tal; el 1er ínidice tiene la información del listado como # página etc
        id = i['id']#se almacena la abreviación en una variable aparte para que me sea más legible
        name = str(i['name'])#guarda el nombre completo del país en una variable aparte por la misma razón
        ids.append(id) # se crea una lista con los ids
        names.append(name) # se crea una lista con los nombres completos
        idsYnames[id] = name # y un diccionario que combina ambos
    return ids, names, idsYnames #lista, lista, diccionario
    

def capitalEs(url,pais):
    response = requests.get(dar_formato(url,id=pais))#consulta a la API por el país especificado
    result = response.json()
    capital = result[1][0]['capitalCity']#busca la key con el nombre de la capital
    pais = idsYnames[pais] #busca en el dicconario "idsYnames" para encontrar el nombre completo del país seleccionado
    return pais,capital


def poblacion(url,pais,fecha=""):#fecha es opcional, también puede ser un rango de fechas de la forma AAAA:AAAA
    response = requests.get(dar_formato(url,id=pais,indicator="/indicator/SP.POP.TOTL",date="&date="+fecha))#consulta a la API el indicador de población del país seleccionado correspondiente a la fecha seleccionada o desde el principio de la base de datos(1973) si se deja en blanco
    result = response.json()
    return result[1]#el primer índice trae la información de los resultados(total de resultados, páginas de resultados etc) por eso se usa el segundo índice que es el que trae los datos como tal


def poblacion_femenina(url,pais,fecha=""):#fecha es opcional, también puede ser un rango de fechas de la forma AAAA:AAAA
    response = requests.get(dar_formato(url,id=pais,indicator="/indicator/SP.POP.TOTL.FE.IN",date="&date="+fecha))#consulta a la API por indicador del país seleccionado 
    result = response.json()
    return result[1]

    
def poblacion_masculina(url,pais,fecha=""):#fecha es opcional, también puede ser un rango de fechas de la forma AAAA:AAAA
    response = requests.get(dar_formato(url,id=pais,indicator="/indicator/SP.POP.TOTL.MA.IN",date="&date="+fecha))#consulta a la API por indicador del país seleccionado 
    result = response.json()
    return result[1]







#↓↓↓ ↓↓↓ ↓↓↓   ignorar   ↓↓↓ ↓↓↓ ↓↓↓


#--------------   for testin'   --------------#
if __name__ == "__main__":
    #sufijos = ["(IBRD-only countries)","(IFC classification)", "IBRD countries classified as high income","(IDA-eligible countries)","(excluding high income)","IDA countries in Sub-Saharan Africa not classified as fragile situations","(IDA & IBRD countries)"]
    
    idsent, nombres, todo_junto = listar_paisesXprimera_vez(url_para_pruebas)
    dato='CRI'
    if dato in ids:
        poblacionf = poblacion_masculina(url_para_pruebas,dato)
        
        for anno in poblacionf:
            print(anno['date'], anno['value'])
        #
    
