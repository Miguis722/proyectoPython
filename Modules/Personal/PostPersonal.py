from tabulate import tabulate
import os
import re
import json
import requests

#Servidor de Personal
def getAllDataPersonal():
	peticion = requests.get("http://154.38.171.54:5503/personas")
	data= peticion.json()
	return data

def nuevaDataDePersonal():
    id = []
    for val in getAllDataPersonal():
        id.append(val.get('id'))
    if id:
        return max(id) + 1
    else:
        return 1

#Deseamos agregar a un personal nuevo a la base de datos.
def NewPersonalInBase():
    Personal = {}
    while True:
        try:
            if not Personal.get("nroId (CC, Nit)"):
                CC = input("Ingrese el CC o NIT del personal: ")
                if re.match(r'^[0-9]+$', CC):
                    Data = getAllDataPersonal()
                    if Data:
                        print(tabulate(Data, headers="keys", tablefmt="rounded_grid"))
                        raise Exception("Este Usuario de Personal ya existe.")
                    else:
                        Personal["nroId (CC, Nit)"] = CC
                        print("El Usuario que desea agregar cumple con los parametros.")
                else:
                    raise Exception("El Usuario no cumple con el patrón establecido, intentelo nuevamente.")
                
            if not Personal.get("Nombre"):
                Nombre = input("Ingrese el Nombre del personal:")
                if re.match(r'^[A-Za-z\s]+$', Nombre):
                    Data = getAllDataPersonal()
                    if Data:
                        print(tabulate(Data, headers="keys", tablefmt="rounded_grid"))
                        raise Exception("Ya hay un usuario registrado con este nombre, intente con otro.")
                    else:
                        Personal["Nombre"] = Nombre
                        print("El nombre cumple con el patrón establecido.")
                else:
                    raise Exception("El Nombre no cumple con el patrón establecido, intentelo nuevamente.")
                
            if not Personal.get("Email"):
                Email = input("Ingrese el Correo Electronico (Email): ")
                if re.match(r'^[\w\.-]+@[\w\.-]+$', Email):
                    Data = getAllDataPersonal()
                    if Data:
                        print(tabulate(Data, headers="keys", tablefmt="rounded_grid"))
                        raise Exception("Ya existe este correo electronico (Email) registrado, intentelo nuevamente.")
                    else:
                        Personal["Email"] = Email
                        print("El correo electronico (Email) cumple con el patrón establecido.") 
                raise Exception("No se ha podido agregar el nuevo personal, intentelo nuevamente.")
        except Exception as error:
            print(error)



def menu():
	while True:
		os.system('cls' if os.name == 'nt' else 'clear')
		 #Link para sacar el diseño:
        # https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Digital&t=AGREGAR%20ACTIVOS
		print("""
						
				+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+
				|A|G|R|E|G|A|R| |P|E|R|S|O|N|A|L|
				+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+

					0. Si desea volver atrás.
					1. Para continuar.
 		""")
		opcion = input("\nSeleccione una de las opciones: ")
    # Pedimos al usuario ingresar un número para escoger la opción que desea del menú de AGREGAR PERSONAL.
		if re.match(r'^[0-1]$', opcion) is not None:
        # Con esta validación vamos a comprobar que el número que ingrese se encuentre
        # Dentro del parámetro de 0 a 1. Además, de que en caso de que ingrese un
        # número distinto a los posibles, volverá a sacar el mismo menú.
			opcion = int(opcion)  # Lo convertimos a un número entero
        # Empezamos a meter los condicionales para el menú.
        # Si la opción es cero, va al menú anterior (getPersonal).
			if opcion == 0:
				break
            
        # Si el usuario selecciona 1, agregara el nuevo personal.
			elif opcion == 1:
				print(tabulate(NewPersonalInBase()))
				input("Presione 0 (Cero) para volver: ")  # Ponemos un input para que cuando corramos lo que necesitamos no se borre lo que queremos mostrar.
        	# AGREGAR