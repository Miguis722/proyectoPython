import os
import re
import requests
from tabulate import tabulate
import json
import Modules.Personal.crudPersonal as CRUDPersonal
import Modules.Personal.delPersonal as DELPersonal
import Modules.Personal.PostPersonal as PostPersonal


#Servidor de Personal
def getAllDataPersonal():
	peticion = requests.get("http://154.38.171.54:5501/personas")
	data= peticion.json()
	return data


def submenu():
     print("""
           ¿Que deseas visualizar?

           1. Todo el personal.
           2. Buscar un personal en especifico.""")
     opcion = input("\nSeleccione una de las opciones: ")
     if re.match(r'^[1-5]$', opcion) is not None:
          opcion = int(opcion)
          if opcion == 1:
            print(tabulate(getAllDataPersonal(), headers="keys", tablefmt="rounded_grid"))
            input("Presione 0 (Cero) para volver: ")#Ponemos un input para que cuando corramos lo que necesitamos no se borre lo que queremos mostrar.
          elif opcion == 2:
            id = input("Ingrese el ID o CC a buscar: ")
            print(tabulate(GetAllDataPersonalXcode(id),headers="keys", tablefmt = "rounded_grid"))
            input("Presione 0 (Cero) para volver: ")#Ponemos un input para que cuando corramos lo que necesitamos no se borre lo que queremos mostrar.
               
def GetAllDataPersonalXcode(id):
    Personal = []
    try:
        for val in getAllDataPersonal():
            #Buscaremos  el personal por su id o por su identificador (cedula de ciudadania)
            if val.get('nroId (CC, Nit)') == id or val.get('id') == id:
                 Personal.append({
                    "id": "2",
                    "nroId (CC, Nit)": val.get('nroId (CC, Nit)'),
                    "Nombre": val.get('Nombre'),
                    "Email": val.get('Email'),
                    "Telefonos de contacto": val.get('Telefonos')
                  })
        if not Personal:
            raise Exception("El número de ID o número de identificacion suministrado no se encuentra en la base de datos existente, verifique porfavor.")
        return Personal
    except Exception as error:
         print(error)
            
                 

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
                
                +-+-+-+-+ +-+ +-+-+-+-+-+-+-+-+
                |M|E|N|U| |-| |P|E|R|S|O|N|A|L|
                +-+-+-+-+ +-+ +-+-+-+-+-+-+-+-+

              
            OPCIONES
                1. AGREGAR
                2. EDITAR
                3. ELIMINAR
                4. BUSCAR
                5. REGRESAR AL MENU PRINCIPAL

              """)
        opcion = input("\nSeleccione una de las opciones: ")
        #Pedimos al usuario ingresar un número para escoger la opción que desea del menú de PERSONAL
        if re.match(r'^[1-5]$', opcion) is not None:
            #Con esta validación vamos a comprobar que el número que ingrese se encuentre
            #Dentro del parametro de 1 a 7. Además, de que en caso de que ingrese un 
            #número distinto a los posibles, volvera a sacar el mismo menú.
            opcion = int(opcion)  # Lo convertimos a un número entero
            #Empezamos a meter los condicionales para el menú.
        if (opcion == 1):
            PostPersonal.menu()
        #Agregar
        elif (opcion == 2):
            CRUDPersonal.menu()
            #Editar
        elif (opcion == 3):
            DELPersonal.menu()
            #Eliminar
        elif (opcion == 4):
            submenu()
            #Buscar
        elif(opcion == 5):
            break
        #Volver al menú principal