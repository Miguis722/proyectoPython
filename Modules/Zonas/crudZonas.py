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



def updateZonas(id):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        data = getAllDataZonas()
        if len(data):
            print("Zona encontrada")
            print(tabulate([data], headers="keys", tablefmt="rounded_grid"))
            for item in data:
                if item["nombreZona"] == id:
                    while True:
                        try:
                            print(""" ¿Qué dato deseas modificar? 
                                0. Volver atrás
                                1. Nombre
                                2. Capacidad Máxima de la zona
                            """)
                            opcion = input("\nSeleccione una de las opciones: ")
                            if re.match(r'^[0-2]$', opcion) is not None:
                                opcion = int(opcion)
                                if opcion == 0:
                                    break
                                elif opcion == 1:
                                    while True:
                                        try:
                                            nombre = input("Ingrese el Nombre de la Zona: ")
                                            if re.match(r'^[A-Za-z\s]+$', nombre) is not None:
                                                item["nombreZona"] = nombre
                                                break
                                            else:
                                                raise Exception("El Nombre de la Zona no cumple con el patrón establecido.")
                                        except Exception as error:
                                            print(error)
                                elif opcion == 2:
                                    while True:
                                        try:
                                            capacidad = input("Ingrese la capacidad máxima de la zona: ")
                                            if re.match(r'^\d+$', capacidad) is not None:
                                                capacidad = int(capacidad)
                                                item["totalCapacidad"] = capacidad
                                                break
                                            else:
                                                raise Exception("La capacidad máxima debe ser un número entero, por favor verifique.")
                                        except Exception as error:
                                            print(error)
                                else:
                                    raise Exception("Opción no válida, por favor seleccione una opción del menú.")
                        except Exception as error:
                            print(error)
                            
                    # Después de que el usuario actualice los datos, realizamos la solicitud PUT al servidor
                    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
                    url = f"http://154.38.171.54:5502/zonas/{item['nombreZona']}"
                    peticion = requests.put(url, headers=headers, data=json.dumps(item))
                    data = peticion.json()
                    return [data]
							

def menu():
	while True:
		os.system('cls' if os.name == 'nt' else 'clear') or ("clear")
		 #Link para sacar el diseño:
        # https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Digital&t=AGREGAR%20ACTIVOS
		print("""
						
				
                    
                        +-+-+-+-+-+-+ +-+-+-+-+-+
                        |E|D|I|T|A|R| |Z|O|N|A|S|
                        +-+-+-+-+-+-+ +-+-+-+-+-+



					0. Si desea volver atrás.
					1. Para continuar.
 		""")
		opcion = input("\nSeleccione una de las opciones: ")
    # Pedimos al usuario ingresar un número para escoger la opción que desea del menú de EDITAR ZONAS
		if re.match(r'^[0-1]$', opcion) is not None:
        # Con esta validación vamos a comprobar que el número que ingrese se encuentre
        # Dentro del parámetro de 0 a 1. Además, de que en caso de que ingrese un
        # número distinto a los posibles, volverá a sacar el mismo menú.
			opcion = int(opcion)  # Lo convertimos a un número entero
        # Empezamos a meter los condicionales para el menú.
        # Si la opción es cero, va al menú anterior (getZonas).
			if opcion == 0:
				break
            
        # Si el usuario selecciona 1, agregara la nueva zona en la base de datos.
			elif opcion == 1:
				id = input("Introduzca el Nombre de la zona la cual desea modificar: ")
				print(tabulate(updateZonas(id), headers="keys", tablefmt="rounded_grid"))
				input("Presione 0 (Cero) para volver: ")  # Ponemos un input para que cuando corramos lo que necesitamos no se borre lo que queremos mostrar.
        	# EDITAR