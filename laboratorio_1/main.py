from Trig import *

operaciones = Trig()  #instanciacion de la clase

ok = False      #variable para el bucle de control, si continua o no
salir = False   #variable para el bucle principal y finalizar el programa
operacion = ''  #para "recordar" cual operacion se hizo

while salir == False: #bucle general, se repite hasta que se seleccione salir
    
  print("¿Que valor desea consultar?\n", # muestra el menú
        "1. Seno de PI\n",
        "2. Coseno de PI\n",
        "4. Salir\n")
    
  while ok == False:  # bucle para comprobar que el # digitado sea un entero válido de lo contrario no continua hasta que lo sea
    try:
      seleccion = int(input())    #trasforma el tipo de variable
      if seleccion <1 or seleccion >4:  #compara el valor para definir si se continua o no
        print("!!!  debe seleccionar una opción válida  !!!\n",
              "1. Seno de PI\n",
              "2. Coseno de PI\n",
              "3. Tangete de PI\n",
              "4. Salir")          
      else:
        ok = True # si el input es válido termina el bucle de comprobación
    except ValueError:
      print("!!!  debe seleccionar una opción válida  !!!\n",
            "1. Seno de PI\n",
            "2. Coseno de PI\n",
            "3. Tangete de PI\n")

  match seleccion: #toma de decisión segun la opción seleccionada
    case 1:
      resultado = operaciones.senoPI()  
      print("El seno de PI corresponde a:",resultado)
      operacion = "seno        "
    case 2:
      resultado = operaciones.cosenoPI()
      operacion = "coseno      "
    case 3:
      resultado = operaciones.tangentePI()  
      print("La tangente de PI corresponde a:",resultado)
      operacion = "tangente    "
    case 4:
      salir = True

  if seleccion != 4: # si no seleccionó "salir" continua el resto del código
    archivo = open("log.txt",'a+')
    tiempo = str(datetime.datetime.now())
    archivo.write("momento: "+tiempo+"   operacion_realizada: "+operacion+"resultado: "+ str(resultado)+'\n') # junta todos los datos para escribir en el log
    archivo.close()

    print("¿Desea continuar?\n", "1. Si     2. No")
    continuar = input()
    if continuar == '1':
      seleccion = 0 # reinicia las variables
      ok = False
      os.system('cls')    #depeja la consola
    else:
      salir = True # finaliza el bucle general y por tanto el programa

