from tabulate import tabulate
import os
import re
import json
import requests
import Modules.Personal.getPersonal as GetPer

#Servidor de Personal
def getAllDataPersonal():
	peticion = requests.get("http://154.38.171.54:5502/personas")
	data= peticion.json()
	return data

#Deseamos editar la información de un personal ya existente en la base de datos.
def modifyAPersonalxd(id):
	while True:
		os.system("cls") or ("clear")
		data =  getAllDataPersonal()
		if len(data):
			print("Personal Encontrado")
			print(tabulate([data], headers="keys", tablefmt="rounded_grid"))
			for item in data:
				if item["nroId (CC, Nit)"] == id:
					continuarActualizar = True
			while continuarActualizar:
				try:
					print("""
							¿Que dato deseas cambiar?
		   
		   				0. Volver atrás.
		   
		   				1. Nombre
		   				2. Email
		   				3. Telefono
					 """)
					opcion = input("\nSeleccione una de las opciones: ")
					if re.match(r'^[0-3]$', opcion) is not None:
						opcion = int(opcion)
						#Si el usuario escoge el número cero (0), lo devolvera al menú. 
						#Pensando en que la persona puede que se equivocara y desee volver al menú.                
						if (opcion == 0):
							break

						elif (opcion ==1):
							while True:
								try:
									Nombre = input("Ingrese el Nombre: ")
									if re.match(r'^[A-Za-z\s]+$', Nombre):
										data["Nombre"] = Nombre
										break
									else:
										raise Exception("El nombre no cumple con el patrón establecido.")
								except Exception as error:
									print(error)
						elif (opcion == 2):
							while True:
									Email = input("Ingre el Email: ")
									data["Email"] = Email
									break
						if (opcion == 3):
							while True:
								try:
									telefono = input("Ingrese el telefono: ")
									if(re.match(r"^[0-9\s-]+$", telefono) is not None):
										data["Telefonos"] = telefono
										break
									else: raise Exception ("El telefono no cumple con el patrón establecido.")
								except Exception as error:
									print(error)
					raise Exception("No se pudo realizar el cambio, intentelo nuevamente.")
				except Exception as error:
					print(error)

def menu():
	while True:
		os.system("cls") or ("clear")
		 #Link para sacar el diseño:
        # https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Digital&t=AGREGAR%20ACTIVOS
		print("""
		+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+
		|E|D|I|T|A|R| |P|E|R|S|O|N|A|L|
		+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+

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
				GetPer.menu()

            # al usar el codigo de break para poder volver al menú de getActivos daba error, por lo que
            # Para solucionarlo y no quedarme sin opciones, decidi importar getPersonal.
            
        # Si el usuario selecciona 1, modificara/editara los datos.
			elif opcion == 1:
				Id = input("Ingrese el CC o NIT del personal que desea modificar: ")
				print(tabulate(modifyAPersonalxd(id)))
				input("Presione 0 (Cero) para volver: ")  # Ponemos un input para que cuando corramos lo que necesitamos no se borre lo que queremos mostrar.
        	# Editar