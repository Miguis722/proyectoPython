import os
import re
import requests
import crudActivos as CRDActivos #Crud activos se encargara de la funcionalidad de EDITAR los activos de la base de datos.
import delActivos as DELETEActivos #Se encargara de la funcionalidad de ELIMINAR un activo de la base de datos.
import PostActivos as PostActivos #Se encargara de la funcionalidad de AGREGAR  un nuevo Activo a la base de datos.


#Servidor de Activos
def getAllDataActivos():
	peticion = requests.get("http://154.38.171.54:5502/activos")
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
             print("Hola Mundo")
            #Agregar
        elif (opcion == 2):
            CRDActivos.menu()
            #Editar
        #elif (opcion == 3):
            #Eliminar
        #lif (opcion == 4):
            #Buscar
        elif(opcion == 5):
            break
        #Volver al menú principal