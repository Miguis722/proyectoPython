from tabulate import tabulate

import re
import os
import sys
import json
import requests
#Empezamos importando las primeras funciones que necesitaremos en un futuro
#Empezaremos haciendo un menú de bienvenida a los usuarios y más adelante podremos importar el resto de procesos.




if (__name__ == '__main__'):
#def menuPrincipal():
    while True:
        #CLS se usa en vez del CLEAR, debido a que uso Windows y no Linux.
        os.system("cls")
        #Sacamos el diseño del Menú principal
        # https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Small%20Keyboard&t=Menu%20Principal

        print("""
                                MENÚ PRINCIPAL

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