from tabulate import tabulate
import re
import os
import re
import json
import requests
#Date time es la libreria que se encarga de trabajar con fechas y horas.
from datetime import date


#Servidor de Activos
def getAllDataActivos():
	peticion = requests.get("http://154.38.171.54:5502/activos")
	data = peticion.json()
	return data

# Función para obtener datos de un activo específico por su ID
def getIdActi2(idActivos):
    for val in getAllDataActivos():  # Itera sobre todos los activos
        if val.get("id") == idActivos:  # Si encuentra el activo con el ID proporcionado
            return val   # Devuelve los datos de ese activo

#Servidor de Personal
def getAllDataPersonal():
  peticion=requests.get("http://154.38.171.54:5503/personas")
  data= peticion.json()
  return data

# Función para obtener los nombres e IDs de todas las personas
def getAllNombrePer():
    persoNombre = []
    for val in getAllDataPersonal():
        name = val.get("Nombre")
        idPer = val.get("id")
        persoNombre.append((name, idPer)) # Agrega el nombre y el ID de cada persona a la lista
    return persoNombre

#Servidor de Zonas
def getAllDataZonas():
  peticion=requests.get("http://154.38.171.54:5503/zonas")
  data= peticion.json()
  return data

# Función para obtener los nombres e IDs de todas las zonas
def getAllNombreZon():
    zonaNombre = []
    for val in getAllDataZonas():
        nameZ = val.get("nombreZona")
        idZon = val.get("id")
        zonaNombre.append((nameZ, idZon)) # Agrega el nombre y el ID de cada zona a la lista
    return zonaNombre

# Función para obtener la asignación de un activo por su número de asignación
def getAsignacion(numAsig):
    activos = getAllDataActivos() # Obtiene todos los activos
    
    for val in activos:
        asignaciones = val.get("asignaciones", [])
        for val in asignaciones:
            if (val.get("NroAsignacion") == numAsig): # Si encuentra la asignación con el número proporcionado
                return [val]  # Devuelve los datos de esa asignación
                
# Función para asignar un activo a una persona o zona
def postAsig(id):
    activos = getIdActi2(id) # Obtiene los datos del activo con el ID proporcionado
    
    if activos: # Si el activo existe 
        while True:
         
            if activos["idEstado"] != "0": # Si el activo no tiene idEstado "0", imprime el mensaje y rompe el ciclo
                print("Este activo ya tiene asignación, no se puede volver a asignar.")
                break
            else:
                # Si el activo si tiene idEstado "0" ejecuta esta parte
                try:
                    activos["idEstado"] = "1" # Cambia el estado del activo a asignado

                    # Solicita los detalles de la asignación al usuario
                    nroAsignacion = input("Ingrese un numero para la asignacion: ")
                    if (re.match(r'^[0-9]+$', nroAsignacion)):
                        nroAsignacion = str(nroAsignacion)
                    else:
                        raise Exception("El numero ingresado no cumple con el estandar, intentelo denuevo")
                    
                    # Con la libreria data time efectua en la variable fechaAsignacion
                    fechaAsignacion = str(date.today())
                    
                    # Verifica si la asignación es para una persona o una zona
                    tipoAsignacion = input("Ingrese el Tipo de Asignacion (Personal / Zona): ")
                    if re.match(r'^(Personal|Zona)$', tipoAsignacion ):
                        tipoAsignacion = tipoAsignacion
                    else:
                        raise Exception("Asignacion no válida. Por favor, ingrese 'Personal' o 'Zona', empezando con Mayuscula.") 

                    if (tipoAsignacion == "Personal"):
                        # Muestra los nombres e IDs de todas las personas y solicita al usuario que ingrese el ID de la persona
                        asignadoA =  input("Ingrese id de la Persona a la que desea asignar:\n" + "".join([f"\t{i}. {val}\n" for i, val in enumerate(getAllNombrePer())]))
                        if(re.match(r'^[0-9]+$', asignadoA)):
                            asignadoA = str(asignadoA)
                    
                    elif (tipoAsignacion == "Zona"):
                        # Muestra los nombres e IDs de todas las zonas y solicita al usuario que ingrese el ID de la zona
                        asignadoA =  input("Ingrese el id de la Zona a la que desea asignar:\n" + "".join([f"\t{i}. {val}\n" for i, val in enumerate(getAllNombreZon())]))
                        if(re.match(r'^[0-9]+$', asignadoA)):
                            asignadoA = str(asignadoA)

                    # Actualiza los datos de asignación y el historial del activo
                    activos["asignaciones"] = [
                        {
                            "NroAsignacion": nroAsignacion,
                            "FechaAsignacion": fechaAsignacion,
                            "TipoAsignacion": tipoAsignacion,
                            "AsignadoA": asignadoA
                        }
                    ]
                    idHitor = "1"
                    activoMovi = activos["idEstado"]
                    activos["historialActivos"] = [            
                        {
                            "NroId": idHitor,
                            "Fecha": fechaAsignacion,
                            "tipoMov": activoMovi,
                            "idRespMov": "6ee3"
                        }
                    ]
                    # Realiza la solicitud PUT para actualizar los datos del activo
                    peticion = requests.put(f"http://154.38.171.54:5503/activos/{id}", data=json.dumps(activos))
                    if(peticion.status_code == 200):
                        return print("La asignacion ha sido realizada correctamente")
                    break # Se sale del bucle while para continuar con el menu principal
                   
                except Exception as error:
                    # Se imprime un mensaje de error indicando que ha ocurrido un error.
                        print('-ERROR-')
                        print(error)
            # Se sale del bucle
            break                
    else:
        print(f"El activo con el ID: {id} no existe, por favor intetelo denuevo") # Imprime un mensaje indicando que la persona no existe
        return None 

def menu():
	while True:
		os.system('cls' if os.name == 'nt' else 'clear')
		 #Link para sacar el diseño:
        # https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Digital&t=AGREGAR%20ACTIVOS
		print("""										                               
                        
                    +-+-+-+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+
                    |A|S|I|G|N|A|C|I|O|N| |D|E| |A|C|T|I|V|O|S|
                    +-+-+-+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+

					0. Si desea volver atrás.
					1. Para continuar.
 		""")
		opcion = input("\nSeleccione una de las opciones: ")
    # Pedimos al usuario ingresar un número para escoger la opción que desea del menú de ASIGNAR ACTIVOS
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
				Id = input("Introduzca el ID que desea asignar: ")
				print(tabulate(postAsig(Id), headers="keys", tablefmt="rounded_grid"))
				input("Presione 0 (Cero) para volver: ")  # Ponemos un input para que cuando corramos lo que necesitamos no se borre lo que queremos mostrar.
        	# ASIGNAR UN ACTIVO
menu()
