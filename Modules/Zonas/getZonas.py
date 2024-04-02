import os
import re
import requests
import Modules.Zonas.delZonas as EliminarZona
import Modules.Zonas.crudZonas as EditarZona
import Modules.Zonas.PostZonas as AgregarNuevaZona
from tabulate import tabulate

#Servidor de Zonas
def getAllDataZonas():
	peticion = requests.get("http://154.38.171.54:5502/zonas")
	data= peticion.json()
	return data

def Zonas():
    ZonaN = list()
    for val in getAllDataZonas():
        Zona = dict({
                "ID": val.get('id'), 
                "Nombre de la Zona": val.get('nombreZona'),
                "Capacidad Maxima": val.get('totalCapacidad')
            })
        ZonaN.append(Zona)
    return ZonaN

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') or ("clear")
        print("""
              
                
                +-+-+-+-+ +-+ +-+-+-+-+-+
                |M|E|N|U| |-| |Z|O|N|A|S|
                +-+-+-+-+ +-+ +-+-+-+-+-+

              
            OPCIONES               
                1. AGREGAR
                2. EDITAR
                3. ELIMINAR
                4. BUSCAR
                5. REGRESAR AL MENU PRINCIPAL

              """)
        opcion = input("\nSeleccione una de las opciones: ")
        #Pedimos al usuario ingresar un número para escoger la opción que desea del menú de ZONAS
        if re.match(r'^[1-5]$', opcion) is not None:
            #Con esta validación vamos a comprobar que el número que ingrese se encuentre
            #Dentro del parametro de 1 a 7. Además, de que en caso de que ingrese un 
            #número distinto a los posibles, volvera a sacar el mismo menú.
            opcion = int(opcion)  # Lo convertimos a un número entero
            #Empezamos a meter los condicionales para el menú.
        if (opcion == 1):
            AgregarNuevaZona.menu()
            #Agregar
        elif (opcion == 2):
            EditarZona.menu()
            #Editar
        elif (opcion == 3):
            EliminarZona.menu()
            #Eliminar
        elif (opcion == 4):
            print(tabulate(Zonas(), headers="keys", tablefmt="rounded_grid"))
            input("Presione 0 (Cero) para volver: ")#Ponemos un input para que cuando corramos lo que necesitamos no se borre lo que queremos mostrar.
            #Buscar
        elif(opcion == 5):
            break
        #Volver al menú principal