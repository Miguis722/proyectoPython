from tabulate import tabulate

import os
import re
import json
import requests

# Servidor de Personal
def get_all_data_personal():
    # Realiza una solicitud GET al servidor de personal y devuelve los datos obtenidos en formato JSON
    response = requests.get("http://154.38.171.54:5502/personas")
    return response.json()

def find_personal_by_id(id):
    # Busca un registro de personal por su identificador en los datos obtenidos del servidor
    for person in get_all_data_personal():
        if person.get('nroId (CC, Nit)') == id:
            return person
    print('\nEl personal no existe')
    return None

# Servidor de Activos
def get_all_data_activos():
    # Realiza una solicitud GET al servidor de activos y devuelve los datos obtenidos en formato JSON
    response = requests.get("http://154.38.171.54:5502/activos")
    return response.json()

def find_activo_by_item_number(NroItem):
    # Busca un activo por su número de ítem en los datos obtenidos del servidor
    for item in get_all_data_activos():
        if item.get('NroItem') == NroItem:
            return item
    print('\nEl activo no existe')
    return None

def delete_personal(id):
    # Obtiene los datos del personal con el ID proporcionado
    personal_data = find_personal_by_id(id)
    
    if personal_data:
        # Verifica si el personal tiene asignaciones
        if len(personal_data['asignaciones']) == 0:
            # Si no tiene asignaciones, marca el estado del personal como "0"
            personal_data['idEstado'] = "0"
            # Realiza una solicitud PUT para actualizar los datos del personal
            response = requests.put("http://154.38.171.54:5502/personas", data=json.dumps(personal_data).encode("UTF-8"))
            if response.status_code == 200:
                print("El personal ha sido eliminado exitosamente.")
            else:
                print("Hubo un problema al intentar eliminar el personal.")
        else:
            print("El personal que está intentando eliminar está asignado, por lo tanto no se puede eliminar.")
    else:
        print("No se encontró al personal con el ID especificado.")

    # Espera la entrada del usuario para volver
    input("Presione Enter para volver: ")

#Hacemos el Menú
def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
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
            print(tabulate(delete_personal(NroItem)))
            input("Presione 0 (Cero) para volver: ")  # Ponemos un input para que cuando corramos lo que necesitamos no se borre lo que queremos mostrar.
        #Eliminar