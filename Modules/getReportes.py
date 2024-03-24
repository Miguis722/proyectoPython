import os
import re
import requests
from tabulate import tabulate

#Servidor de Reportes
def getAllDataReportes():
	peticion = requests.get("http://")
	data= peticion.json()
	return data


         
     
def menu():
    while True:
        os.system("cls")
        print("""

                +-+-+-+-+ +-+ +-+-+-+-+-+-+-+-+
                |M|E|N|U| |-| |R|E|P|O|R|T|E|S|
                +-+-+-+-+ +-+ +-+-+-+-+-+-+-+-+

              
            OPCIONES 
                1. LISTAR TODOS LOS ACTIVOS
                2. LISTAR ACTIVOS POR CATEGORIA
                3. LISTAR ACTIVOS DADOS POR BAJA POR DAÑO
                4. LISTAR ACTIVOS Y ASIGNACION
                5. LISTAR HISTORIAL DE MOV. DE ACTIVO
                6. REGRESAR AL MENU PRINCIPAL

              """)
        
        opcion = input("\nSeleccione una de las opciones: ")
        #Pedimos al usuario ingresar un número para escoger la opción que desea del menú de REPORTES
        if re.match(r'^[1-6]$', opcion) is not None:
            #Con esta validación vamos a comprobar que el número que ingrese se encuentre
            #Dentro del parametro de 1 a 7. Además, de que en caso de que ingrese un 
            #número distinto a los posibles, volvera a sacar el mismo menú.
            opcion = int(opcion)  # Lo convertimos a un número entero
            #Empezamos a meter los condicionales para el menú.
        if (opcion == 1):
            print(tabulate(getAllDataReportes(),headers="keys", tablefmt="rounded_grid"))
            #LISTAR TODOS LOS ACTIVOS
        #elif (opcion == 2):
            #LISTAR ACTIVOS POR CATEGORIA
        #elif (opcion == 3):
            #LISTAR ACTIVOS DADOS POR BAJA POR DAÑO
        #elif (opcion == 4):
            #LISTAR ACTIVOS Y ASIGNACION
        #elif (opcion == 5):
            #LISTAR HISTORIAL DE MOV. DE ACTIVO
        #elif (opcion == 6):
            break
        #Volver al menú principal