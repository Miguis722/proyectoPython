from tabulate import tabulate

import re
import os
import sys
import json
import requests
#Empezamos importando las primeras funciones que necesitaremos en un futuro
#Empezaremos haciendo un menú de bienvenida a los usuarios y más adelante podremos importar el resto de procesos.





def menuPrincipal():
    while True:
        #CLS se usa en vez del CLEAR, debido a que uso Windows y no Linux.
        os.system("cls")
        #Sacamos el diseño del Menú principal
        # https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Small%20Keyboard&t=Menu%20Principal

        print("""
              
 ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ ____ ____ 
||M |||e |||n |||u |||       |||P |||r |||i |||n |||c |||i |||p |||a |||l ||
||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|

              
              1. ACTIVOS
              2. PERSONAL
              3. ZONAS
              4. ASIGNACION DE ACTIVOS
              5. REPORTES
              6. MOVIMIENTO DE ACTIVOS
              7. SALIR

              """)

menuPrincipal()

print(menuPrincipal)