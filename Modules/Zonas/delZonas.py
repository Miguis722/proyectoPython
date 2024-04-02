from tabulate import tabulate
import os
import re
import json
import requests


#Servidor de Zonas
def getAllDataZonas():
	peticion = requests.get("http://154.38.171.54:5502/zonas")
	data= peticion.json()
	return data

def confirmaciondataexistente(id):
    try:
        response = requests.get(f"http://154.38.171.54:5502/zonas/{id}")
        response.raise_for_status()
        return [response.json()]
    except Exception as e:
        print(f"Error: {e}")
        return []

def deleteZonas(id):
        data = confirmaciondataexistente(id)
        if len(data):
            peticion = requests.delete(f"http://154.38.171.54:5502/zonas/{id}")
            if peticion.status_code == 204:
                data.append({"message": "Zona eliminado correctamente"})
                return {
                    "body": data,
                    "status": peticion.status_code,
                }
        else: 
            return{
                    "body": [{
                        "Mensaje": "Zona no encontrada.",
                        "Id": id,
                    }],
                    "status": 400,
                }

def menu():
	while True:
		os.system('cls' if os.name == 'nt' else 'clear')
		 #Link para sacar el diseño:
        # https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Digital&t=AGREGAR%20ACTIVOS
		print("""										                               
                        +-+-+-+-+-+-+-+-+ +-+-+-+-+-+
                        |E|L|I|M|I|N|A|R| |Z|O|N|A|S|
                        +-+-+-+-+-+-+-+-+ +-+-+-+-+-+


					0. Si desea volver atrás.
					1. Para continuar.
 		""")
		opcion = input("\nSeleccione una de las opciones: ")
    # Pedimos al usuario ingresar un número para escoger la opción que desea del menú de ELIMINAR ZONAS
		if re.match(r'^[0-1]$', opcion) is not None:
        # Con esta validación vamos a comprobar que el número que ingrese se encuentre
        # Dentro del parámetro de 0 a 1. Además, de que en caso de que ingrese un
        # número distinto a los posibles, volverá a sacar el mismo menú.
			opcion = int(opcion)  # Lo convertimos a un número entero
        # Empezamos a meter los condicionales para el menú.
        # Si la opción es cero, va al menú anterior (getZonas).
			if opcion == 0:
				break
            
        # Si el usuario selecciona 1, eliminara la zona de la base de datos.
			elif opcion == 1:
				Id = input("Introduzca el Id de la zona la cual desea eliminar: ")
				print(tabulate(deleteZonas(Id), headers="keys", tablefmt="rounded_grid"))
				input("Presione 0 (Cero) para volver: ")  # Ponemos un input para que cuando corramos lo que necesitamos no se borre lo que queremos mostrar.
        	# ELIMINAR
menu()