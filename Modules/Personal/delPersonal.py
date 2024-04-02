from tabulate import tabulate
import os
import re
import json
import requests

#Servidor de Personal
def getAllDataPersonal():
	peticion = requests.get("http://154.38.171.54:5502/personas")
	data= peticion.json()
	return data

def ANumeroDePersonal(id):
    PersonalEncontrados = []
    for val in getAllDataPersonal():
        if val.get('nroId (CC, Nit)') == id:
            PersonalEncontrados.append(val)
            return PersonalEncontrados
    print('\nEl personal no existe')
    return PersonalEncontrados

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


# NO SE PUEDE ELIMINAR PERSONAS QUE CUENTEN CON ACTIVOS ASIGNADOS.
#Deseamos eliminar un personal ya existente de la base de datos.
def deletePersonal(id):
    data =  ANumeroDePersonal(id), ActivosNumeroDeItem()
    if len(data):
            while True:
                os.system('cls' if os.name == 'nt' else 'clear') or ("clear")
                try:
                    if len(data[0]['asignaciones']) == 0:
                        data[0]['idEstado'] = "0"
                    else:
                        raise Exception("El personal que está intentando eliminar está asignado, por lo tanto no se puede eliminar.")                        
                except Exception as error:
                    print(error)
                break
            peticion = requests.put(f"http://154.38.171.54:5502/personas", data=json.dumps(data[0]).encode("UTF-8"))
            res = peticion.json()
            if 'Mensaje' in res:
                print(res['Mensaje'])
            input("Presione 0 (Cero) para volver: ")
            return [res]
    
def menu():
	while True:
		os.system('cls' if os.name == 'nt' else 'clear') or ("clear")
		 #Link para sacar el diseño:
        # https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Digital&t=AGREGAR%20ACTIVOS
		print("""
		
        +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+
        |E|L|I|M|I|N|A|R| |P|E|R|S|O|N|A|L|
        +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+


		0. Si desea volver atrás.
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
        # Si la opción es cero, va al menú anterior (getPersonal).
			if opcion == 0:
				break
            
        # Si el usuario selecciona 1, eliminara el personal según su id.
			elif opcion == 1:
				Id = input("Ingrese el CC o NIT del personal que desea modificar: ")
				print(tabulate(deletePersonal(Id)))
				input("Presione 0 (Cero) para volver: ")  # Ponemos un input para que cuando corramos lo que necesitamos no se borre lo que queremos mostrar.
        	# Editar
  