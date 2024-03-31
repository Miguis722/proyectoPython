from tabulate import tabulate

import re
import os
import sys
import json
import requests
#Empezamos importando las primeras funciones que necesitaremos en un futuro
#Empezaremos haciendo un menú de bienvenida a los usuarios y más adelante podremos importar el resto de procesos.
import Modules.Activos.getActivos as Activos
import Modules.Asignacion.getAsignacion as Asignacion
import Modules.Movimientos.getMovimiento as Movimientos
import Modules.Personal.getPersonal as Personal
import Modules.Reportes.getReportes as Reportes
import Modules.Zonas.getZonas as Zonas
#Importaremos de donde se está sacando toda la información, además le asignaremos un nombre en especial para hacernos más facil
#La tarea de redireccionar a los usuarios.


#Usaremos __main__ para nombrar el menú. Ya que será lo primero que se nos mostrara, evitando que salgan otras cosas no deseadas.
if (__name__ == '__main__'):
#def menuPrincipal():
    while True:
        #CLS se usa en vez del CLEAR, debido a que uso Windows y no Linux.
        os.system("cls") or ("clear")
        #Sacamos el diseño del Menú principal
        # https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Small%20Keyboard&t=Menu%20Principal

        print("""
                               
                        +-+-+-+-+ +-+-+-+-+-+-+-+-+-+
                        |M|e|n|u| |P|r|i|n|c|i|p|a|l|
                        +-+-+-+-+ +-+-+-+-+-+-+-+-+-+


                    SISTEMA G&C DE INVENTARIO CAMPUSLANDS
              
        OPCIONES  
              1. ACTIVOS
              2. PERSONAL
              3. ZONAS
              4. ASIGNACION DE ACTIVOS
              5. REPORTES
              6. MOVIMIENTO DE ACTIVOS
              7. SALIR
              """)
#Es importante poner un tiempo final para que no siga apareciendo en bucle.
#Ya que puede hacer que el dispositivo se trabe o deje de funcionar optimamente.
        opcion = input("\nSeleccione una de las opciones: ")
        #Pedimos al usuario ingresar un número para escoger la opción que desea del menú
        if re.match(r'^[1-7]$', opcion) is not None:
            #Con esta validación vamos a comprobar que el número que ingrese se encuentre
            #Dentro del parametro de 1 a 7. Además, de que en caso de que ingrese un 
            #número distinto a los posibles, volvera a sacar el mismo menú.
            opcion = int(opcion)  # Lo convertimos a un número entero
            #Empezamos a meter los condicionales para el menú.
        if (opcion == 1):
            Activos.menu()
        elif (opcion == 2):
            Personal.menu()
        elif (opcion == 3):
            Zonas.menu()
        elif (opcion == 4):
            Asignacion.menu()
        elif(opcion == 5):
            Reportes.menu()
        elif(opcion == 6):
            Movimientos.menu()
        elif(opcion == 7):
            exit()

#Ponemos las condiciones de que solo puede seleccionar del número de entre 1 y 7, si no escoge  uno de estos, volvera a aparecer el mismo
            #Menú, hasta que escoja un número valido.
    