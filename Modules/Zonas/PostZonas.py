from tabulate import tabulate
import os
import re
import json
import requests

#Servidor de Zonas
def getAllDataZonas():
	peticion = requests.get("http://154.38.171.54:5501/zonas")
	data= peticion.json()
	return data


def nuevaDataDeZonas():
    id = []
    for val in getAllDataZonas():
        id.append(val.get('id'))
    if id:
        return max(id) + 1
    else:
        return 1
    
#Deseamos agregar una nueva zona a la base de datos.
def NewZonaInBase():
    Zona = {}
    while True:
        try:
            if not Zona.get('nombreZona'):
                NombreDeLaZona = input("Ingrese el nombre de la zona: ")
                if re.match(r'\w+', NombreDeLaZona) is None:
                    NombreDeLaZona =str(NombreDeLaZona)
                    Data = getAllDataZonas()
                    if Data:
                        print(tabulate(Data, headers="keys", tablefmt="rounded_grid"))
                        raise Exception("El nombre de la zona ya existe.")
                    else:
                        Zona['nombreZona'] = NombreDeLaZona
                        print("El nombre de la zona que desea agregar cumple con los parametros.")
                else:
                    raise Exception("El nombre de la zona no cumple con el patrón establecido, intentelo nuevamente.")
                
            if not Zona.get('totalCapacidad'):
                CapacidadMaxima = input("Ingrese la Capacidad Maxima de la Zona: ")
                if re.match(r'^[0-9]+$', CapacidadMaxima) is None:
                    Zona['totalCapacidad'] = int(CapacidadMaxima)
                else:
                    print("Solo se permiten números.")
                    
            raise Exception("No se ha podido agregar una nueva zona, intentelo nuevamente.")
            
        except Exception as error:
            print(error)

        Zona ={
             "Nombre de la Zona": (NombreDeLaZona),
             "Capacidad Maxima de la zona": (CapacidadMaxima)
        }
        headers = {'Content-type': 'aplication/json', 'chatset': 'UTF-8'}
        peticion = requests.post("http://154.38.171.54:5501/zonas", headers=headers, data=json.dumps(Zona))
        res = peticion.json()
        res["Mensaje"] = "Se agrego correctamente la zona."
        return [res]


def menu():
	while True:
		os.system('cls' if os.name == 'nt' else 'clear')
		 #Link para sacar el diseño:
        # https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Digital&t=AGREGAR%20ACTIVOS
		print("""
						
				
                    +-+-+-+-+-+-+-+ +-+-+-+-+
                    |A|G|R|E|G|A|R| |Z|O|N|A|
                    +-+-+-+-+-+-+-+ +-+-+-+-+


					0. Si desea volver atrás.
					1. Para continuar.
 		""")
		opcion = input("\nSeleccione una de las opciones: ")
    # Pedimos al usuario ingresar un número para escoger la opción que desea del menú de AGREGAR ZONAS
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
				print(tabulate(NewZonaInBase(), headers="keys", tablefmt="rounded_grid"))
				input("Presione 0 (Cero) para volver: ")  # Ponemos un input para que cuando corramos lo que necesitamos no se borre lo que queremos mostrar.
        	# AGREGAR