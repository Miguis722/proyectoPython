from tabulate import tabulate

import os
import re
import json
import requests

#Servidor de Activos
def getAllDataActivos():
	peticion = requests.get("http://154.38.171.54:5502/activos")
	data = peticion.json()
	return data

def ActivosNumeroDeItem(NroItem):
    ItemEncontrados = []
    for val in getAllDataActivos():
        if val.get('NroItem') == NroItem:
            ItemEncontrados.append(val)
            return ItemEncontrados
    print('\nEl activo no existe')
    return ItemEncontrados

#Deseamos eliminar un activo por medio de su NroItem, tenemos la condición especial de que no se elimina, solo se cambia el estado del activo a NO ASIGNADO o "0"
def deleteActivo(NroItem): 
    
    data = ActivosNumeroDeItem(NroItem)
    if len(data):
        while True:
            os.system("cls") or ("clear")
            try:
                #Comprobamos que en asignaciones no se encuentre asignado a alguna persona o una zona.
                #Si llega a estar asignado saltara el else:. Diciendo que no se puede eliminar.
                if len(data[0]['asignaciones']) == 0:
                    data[0]['idEstado'] = "0"
                else:
                    raise Exception("El activo que está intentando eliminar está asignado a una persona o zona, por lo tanto no se puede eliminar.")                        
            except Exception as error:
                print(error)
                break
    
        peticion = requests.put(f"http://154.38.171.54:5502/activos?NroItem={NroItem}", data=json.dumps(data[0]).encode("UTF-8"))
        res = peticion.json()
        if 'Mensaje' in res:
            print(res['Mensaje'])
        input("Presione 0 (Cero) para volver: ")
        return [res]

#Hacemos el Menú
def menu():
    while True:
        os.system("cls") or ("clear")
        #Link para sacar el diseño:
        # https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Digital&t=AGREGAR%20ACTIVOS
        print("""
              
              
                +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+
                |E|L|I|M|I|N|A|R| |A|C|T|I|V|O|S|
                +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+

               0. Si desea voler atrás.
               1. Para continuar.
               
               """)
        opcion = input("\nSeleccione una de las opciones: ")
        # Pedimos al usuario ingresar un número para escoger la opción que desea del menú de EDITAR ACTIVOS
        if re.match(r'^[0-1]$', opcion) is not None:
        # Con esta validación vamos a comprobar que el número que ingrese se encuentre
        # Dentro del parámetro de 0 a 1. Además, de que en caso de que ingrese un
        # número distinto a los posibles, volverá a sacar el mismo menú.
            opcion = int(opcion)  # Lo convertimos a un número entero
        # Empezamos a meter los condicionales para el menú.
        # Si la opción es cero, va al menú anterior (getActivos).
        if opcion == 0:
            break
            
        # Si el usuario selecciona 1, modificara/editara los datos.
        elif opcion == 1:
            NroItem = (input("Ingrese el NroItem que desea eliminar: "))
            print(tabulate(deleteActivo(NroItem)))
            input("Presione 0 (Cero) para volver: ")  # Ponemos un input para que cuando corramos lo que necesitamos no se borre lo que queremos mostrar.
        #Eliminar