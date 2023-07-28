import requests

def random_joke():#chiste aleatorio, no hace falta usar la biblioteca random porque la api ya incluye una url para eso
    response = requests.get("https://api.chucknorris.io/jokes/random")#obtención del objeto respuesta
    print(response.json()['value'])#decodifica la respuesta, la convierte en una lista y muestra el valor
    return
    

def category_list():
    with requests.get("https://api.chucknorris.io/jokes/categories") as response:#url que contiene la lista de categorías
        return response.json()#convierte la respuesta en lista y la retorna al main
    

def category_joke(lista,categoria):# pide una lista y un número de categoría(índice para la lista)
    with requests.get(f"https://api.chucknorris.io/jokes/random?category={lista[categoria]}") as response:
        print(response.json()['value']) # muestra el valor solicitado
    return


#------------------------     menú     ---------------------#
while True:
    print("\nSeleccione una opción:\n","1. chiste aleatorio\n","2. chiste de una categoría específica\n", "3. salir")
    opcion = input()
    match opcion:
        case '1':
            random_joke()
        case '2':
            lista = category_list()#consigue la lista de categorias
            num=1     #variable para enumerarlas
            for i in lista:  #bucle para enlistar y enumerar las categorias
                print(f" {num}.{i}")
                num += 1
            
            while True: #bucle para validar que el dato digitado sea un número
                try: 
                    cat = int(input("\nElija una categoría   "))-1 #resta uno al número para que coincida con el índice de la lista
                    break
                except ValueError: # para evitar valores incorrectos
                    print("\n!!!   debe seleccionar una opción válida   !!!\n")
            
            if cat >= 0 and cat < 17 : # de nuevo para asegurar que el # este en el rango correcto
                category_joke(category_list(),cat)
            else:
                print("\nCategoría no válida")
        case '3': # case para la opción "salir"
            break
        case _:
            print("\n!!!   debe seleccionar una opción válida   !!!\n")
