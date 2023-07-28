import api
import ids
import time
import aiohttp 
import asyncio


num_user = ids
consulta = api
"""
#-----------------------------------------------------------------------parte síncrona funcional
inicio = time.time()

for x in num_user.ids:                                #por cada índice del array ids
    resultado = consulta.getOneUser(num_user.ids[x]) # guarda el diccionario devuelto en la variable resultado
    print(resultado["name"])                        #extrae y muestra valor del key "name" 

tarda = time.time() - inicio

print(f"Se mostraron {len(num_user.ids)} nombres en {tarda} segundos")
#-----------------------------------------------------------------------parte síncrona funcional

"""






#__________________________________________________________intento de concurrencia imitado (no entiendo nada...)
"""
async def getOneUserAsync(id,session):
    url = "https://jsonplaceholder.typicode.com/users/"
    async with session.get(url) as response:
        dicc = response.json()[id]
        print(dicc["nombre"])
    
async def programa(iterable):
    async with AsyncReq.ClientSession() as session:
        tareas = []
        for user in iterable:
            tarea = asyncio.ensure_future(getOneUserAsync(user,session))
            tareas.append(tarea)
        await asyncio.gather(*tareas, return_exceptions=True)
       
        
inicio = time.time()
asyncio.get_event_loop().run_until_complete(programa(num_user.ids))
tarda = time.time() - inicio

print(f"Se mostraron {len(num_user.ids)} nombres en {tarda} segundos")
"""
#__________________________________________________________intento de concurrencia imitado (no entiendo nada...)





"""
#otra prueba de concurrencia/intentado entender el código

async def programa(): #esta seria como la fucion que se encarga de ciclar la otra funcion 
    async with aiohttp.ClientSession() as algo: #crea un objeto? para que haga algo, no comprendo
        for num in num_user.ids: #intento replicar el comportamiento de ciclar por cada índice como en el código funcional de arriba
            resultado = getOneUserAsync(num, algo)  #guada el resultado de la función que se espera que sea un diccionario
                                                    #y se le manda el índice actual y el resultado de la session
            print(resultado["name"]) #muestra el valor del key "name"


async def getOneUserAsync(id, algo): # recibe el índice de por donde vaya y el resultado de ClientSession()
    url = "https://jsonplaceholder.typicode.com/users/" # una constante
    async with algo.get(url) as response: #guarda en el resultado de ClientSession() lo que está obteniendo con .get que tampoco sé que es
        return await response.json()[id] #lo convierte en un diccionario??


inicio = time.time()                                    # esta parte igual al ejemplo, no funciona...
asyncio.get_event_loop().run_until_complete(programa())
tarda = time.time() - inicio

print(f"Se mostraron {len(num_user.ids)} nombres en {tarda} segundos")





#       toma 20.....



async def programa():
    #valores = []
    tareas = []    # lista para agrupar las co-rutinas para posterior ejecución
    for x in num_user.ids: #bucle para recorrer el módulo de ids 
        tarea = asyncio.create_task(consulta.getOneUserAsync(x)) #crea una tarea para cada solicitud de id
        tareas.append(tarea) # agrega la tarea creada a una lista
        print(x) # solo de referencia, para saber si el programa esta corriendo muestra la iteracion actual
    resultados = await asyncio.gather(*tareas)  #ejecuta todas la tareas en la fila y guarda los resultados
    for y in range(len(resultados)): #bucle para mostrar el valor de la llave "nombre" de cada diccionario en la lista
        print(resultados[y]['name'])
    print("fin de programa") #señal de referencia...
    


inicio = time.time()
asyncio.get_event_loop().run_until_complete(programa())  #no encuentro diferencia en los
#asyncio.run(programa())                                  #los métodos de ejecución
tarda = time.time() - inicio

print(f"Se mostraron {len(num_user.ids)} nombres en {tarda} segundos")


"""



#correccion 

async def programa():
    async with aiohttp.ClientSession() as session: #funcion asíncrona para crear un objeto sesión asíncrono
        tareas = [] #lista para almacenar la corrutinas a ejecutar asíncronamente 
        for i in num_user.ids: #bucle para ejecutar la funcion para cada número de id
            respuesta = consulta.getOneUserAsync(i,session) #ejecuta la función y guarda el resultado la variable
            tareas.append(respuesta) # agrega la variable resultante en la lista 
        results = await asyncio.gather(*tareas)# ejecuta todas la corrutinas de la lista y guarda el resultado en otra lista
        for name in results: # bucle para mostrar los nombres en filas en lugar de la lista chorreada
            print(name)
    print("fin programa") #referencia visual de que el programa está funcionando



inicio = time.time()
#asyncio.get_event_loop().run_until_complete(programa())  #no encuentro diferencia en los
asyncio.run(programa())                                  #los métodos de ejecución
tarda = time.time() - inicio

print(f"Se mostraron {len(num_user.ids)} nombres en {tarda} segundos")
