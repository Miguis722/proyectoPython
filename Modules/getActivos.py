import os
import re
import requests

#Servidor de Activos
def getAllDataActivos():
	peticion = requests.get("http://")
	data= peticion.json()
	return data

def menu():
    while True:
        os.system("cls")
        print("""
              

                +-+-+-+-+ +-+ +-+-+-+-+-+-+-+
                |M|E|N|U| |-| |A|C|T|I|V|O|S|
                +-+-+-+-+ +-+ +-+-+-+-+-+-+-+

              
            OPCIONES 
                1. AGREGAR
                2. EDITAR
                3. ELIMINAR
                4. BUSCAR
                5. REGRESAR AL MENU PRINCIPAL

              """)
        
        opcion = input("\nSeleccione una de las opciones: ")
        #Pedimos al usuario ingresar un número para escoger la opción que desea del menú de ACTIVOS
        if re.match(r'^[1-5]$', opcion) is not None:
            #Con esta validación vamos a comprobar que el número que ingrese se encuentre
            #Dentro del parametro de 1 a 7. Además, de que en caso de que ingrese un 
            #número distinto a los posibles, volvera a sacar el mismo menú.
            opcion = int(opcion)  # Lo convertimos a un número entero
            #Empezamos a meter los condicionales para el menú.
        if (opcion == 1):
            #Agregar
        elif (opcion == 2):
            #Editar
        elif (opcion == 3):
            #Eliminar
        elif (opcion == 4):
            #Buscar
        elif(opcion == 5):
            break
        #Volver al menú principal