import requests
import re
import matplotlib.pyplot as matplot

api_key = "877c2852402ac08287a082bbaaa97aa0"

def APIcall(page):
    url = f'https://api.themoviedb.org/3/search/movie?query=Action&api_key={api_key}&page={page}'
    response = requests.get(url).json()
    return response['results']
    
#☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼
#               para manejo individual de los datos (ignorar)

# names = [x['original_title'] for x in APIcall(299)]
# rating = [x['vote_average'] for x in APIcall(299)]
# release = [x['release_date'].split("-")[0] for x in APIcall(299)]
#☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼ ☼

# listas para almacenar las categorías de datos individualmente
names = []
rating = []
release = []

print("analyzed page: ",end="")
for page in range(1,30): # para ir una por una por las todas las páginas disponibles ya que no encuentro un atributo del endpoint para modificar los resultados por página, el default son 20 resultados /page
    print(page,"✓",end=", ") # feedback visual de que el programa está funcionando
    for x in APIcall(page): # realiza una consulta a la API para cada página
        year = x['release_date'].split("-")[0] # separa el año del key de fecha en la respuesta de la API
        if year == '': continue # se salta la iteración actual cuando la repuesta de la api contiene un espacio vacío y evitar que se caiga el programa en la conversión del string a número
        elif int(year) >= 2000 and re.search(r'\bAction\b',x['original_title']): #filtra los resultados por año y presencia de "Action" en el key 'título'
            rating.append(x['vote_average'])    #son los datos que se usarán en el gráfico
            # names.append(x['original_title'])   # solo para referencia
            # release.append(x['release_date'].split("-")[0])# solo para referencia


totales = [rating.count(x) for x in range(0,11)]# rellena la lista "totales" contando cuantos items de cada valor hay dentro de la lista "rating"

matplot.bar(range(0,11),totales)
matplot.title('Cantidad de películas con la palabra "Action" en el título y su calificación')
matplot.xticks(range(0,11))
matplot.ylabel("Cantidad de películas")
matplot.xlabel("Calificaciones")
matplot.show()









    

# print(response)
# print(names)
# print(rating)
# print(release)
# print("total de nombres",len(names))
# print("total de ratings",len(rating))
# print("total de fechas",len(release))