import os
import re
import requests

#Servidor de Asignacion
def getAllDataAsignacion():
	peticion = requests.get("http://")
	data= peticion.json()
	return data

def menu():
    while True:
        os.system("cls")
        print("""
            
                +-+-+-+-+ +-+ +-+-+-+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+
                |M|E|N|U| |-| |A|S|I|G|N|A|C|I|O|N| |D|E| |A|C|T|I|V|O|S|
                +-+-+-+-+ +-+ +-+-+-+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+


            OPCIONES 
                1. CREAR ASIGNACION
                2. BUSCAR ASIGNACION
                3. REGRESAR AL MENU PRINCIPAL

              """)
        
        opcion = input("\nSeleccione una de las opciones: ")
        #Pedimos al usuario ingresar un número para escoger la opción que desea del menú de ASIGNACION
        if re.match(r'^[1-3]$', opcion) is not None:
            #Con esta validación vamos a comprobar que el número que ingrese se encuentre
            #Dentro del parametro de 1 a 7. Además, de que en caso de que ingrese un 
            #número distinto a los posibles, volvera a sacar el mismo menú.
            opcion = int(opcion)  # Lo convertimos a un número entero
            #Empezamos a meter los condicionales para el menú.
        if (opcion == 1):
            #CREAR ASIGNACIÓN
        #elif (opcion == 2):
            #BUSCAR ASIGNACIÓN
        #elif (opcion == 3):
            break
        #Volver al menú principal