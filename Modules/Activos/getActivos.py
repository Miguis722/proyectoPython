from tabulate import tabulate
import os
import re
import requests
import Modules.Activos.crudActivos as CRUDActivos #Crud activos se encargara de la funcionalidad de EDITAR los activos de la base de datos.
import Modules.Activos.delActivos as DELETEActivos #Se encargara de la funcionalidad de ELIMINAR un activo de la base de datos.
import Modules.Activos.PostActivos as PostActivos #Se encargara de la funcionalidad de AGREGAR  un nuevo Activo a la base de datos.


#Servidor de Activos
def getAllDataActivos():
	peticion = requests.get("http://154.38.171.54:5502/activos")
	data = peticion.json()
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
            print(tabulate(getAllDataActivos(),headers="keys", tablefmt = "rounded_grid"))
            input("Presione 0 (Cero) para volver: ")#Ponemos un input para que cuando corramos lo que necesitamos no se borre lo que queremos mostrar.
          elif opcion == 2:
               id = input("Ingrese el ID a buscar: ")
               print(tabulate(SearchActivo(id),headers="keys", tablefmt = "rounded_grid"))               
               input("Presione 0 (Cero) para volver: ")#Ponemos un input para que cuando corramos lo que necesitamos no se borre lo que queremos mostrar.
            #Buscar

def SearchActivo(id):
    Activos = []
    try:
        for val in getAllDataActivos():
            if val.get('NroItem') == id or val.get('id') == id:
                Activos.append({ 
                        "Identificacion": val.get('NroItem'),
                        "Item N°" : val.get("NroItem"),  
                        "Codigo de Transacción": val.get('CodTransaccion'),
                        "Número de serie": val.get("NroSerial"),
                        "Codigo en Campus": val.get("CodCampus"),
                        "Formulario": val.get('NroFormulario'),
                        "Nombre": val.get('Nombre'),
                        "Proveedor": val.get('Proveedor'),
                        "Responsable": val.get('EmpresaResponsable'),
                        "Id de la marca": val.get('idMarca'),
                        "Id del tipo": val.get('idTipo')
                })
        if not Activos:
            raise Exception("El número ID o El número de Item suministrado no se encuentra en la base de datos existente.")
        return Activos
    except Exception as error:
        print(error)
        



def menu():
    while True:
        #CLS se usa en vez del CLEAR, debido a que uso Windows y no Linux.
        os.system("cls") or ("clear")
        print("""
              

                +-+-+-+-+ +-+ +-+-+-+-+-+-+-+
                |M|E|N|U| |-| |A|C|T|I|V|O|S|
                +-+-+-+-+ +-+ +-+-+-+-+-+-+-+

              
            OPCIONES 
                1. AGREGAR
                2. EDITAR
                3. ELIMINAR
                4. BUSCAR
                5. REGRESAR AL MENU PRINCIPAL

              """)
        
        opcion = input("\nSeleccione una de las opciones: ")
        #Pedimos al usuario ingresar un número para escoger la opción que desea del menú de ACTIVOS
        if re.match(r'^[1-5]$', opcion) is not None:
            #Con esta validación vamos a comprobar que el número que ingrese se encuentre
            #Dentro del parametro de 1 a 7. Además, de que en caso de que ingrese un 
            #número distinto a los posibles, volvera a sacar el mismo menú.
            opcion = int(opcion)  # Lo convertimos a un número entero
            #Empezamos a meter los condicionales para el menú.
        if (opcion == 1):
            PostActivos.menu()
            #Agregar
        elif (opcion == 2):
            CRUDActivos.menu()
            #Editar
        elif (opcion == 3):
            DELETEActivos.menu()
            #Eliminar
        elif (opcion == 4):
            submenu()
            #Buscar
        elif(opcion == 5):
            break
        #Volver al menú principal