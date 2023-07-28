import requests as req


def getOneUser(id): #funcion de respuesta, solo require el consecutivo 
    url = "https://jsonplaceholder.typicode.com/users/" #url de pruebas
    response = req.get(url) #guarda el "responseObject" obtenido por la función "get()"
    return response.json()[id] #devuelve el objeto decodificado en json


async def getOneUserAsync(id,session): #version asíncrona de la anterior requiere el consecutivo y un objeto "session"
    url = "https://jsonplaceholder.typicode.com/users/" #url de pruebas
    async with session.get(url) as objetoSession: #obtiene un objeto sesión para realizar la conexión 
        response = await objetoSession.json() #espera a recibir la respuesta del .get() y decodifica el json
        return response[id]['name'] # devuelve la variable decodificada|converitda en corrutina???
    

    """
    ###_______NOTAS
    Se usa la sintaxis "with" porque además de que hace una funcionalidad parecida al try/catch pero principalmente 
    porque el método de ".get()" de la biblioteca "requests" también tiene un método ".close()" y el "with" se 
    encarga de liberar los recursos EN USO una vez se termina de correr el código, lo mismo para los métodos "open()"
    "write()" etc para leer y modificar archivos

    ".json()" es una función de DECODIFICACIÓN por eso solo funciona si la información solicitada ya está en formato json

    """


    

