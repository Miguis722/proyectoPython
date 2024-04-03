from tabulate import tabulate
import os
import re
import requests

#Servidor de Activos
def getAllDataActivos():
	peticion = requests.get("http://154.38.171.54:5503/activos")
	data = peticion.json()
	return data

#Enlistamos todos los activos con su respectivo codigo de Campus
def getAllActivosCODCAMPUS():
  CODACTIVOSCAMPUS= list()
  for val in getAllDataActivos():
      CODACTIVOSCAMPUS.append({
      "Codigo en Campus": val.get("CodCampus"),
      "Nombre": val.get("Nombre")
       })
  return CODACTIVOSCAMPUS


def getAllActivosCate(categ):
    activosCate= list()
    for val in getAllDataActivos():
        if(val.get("idCategoria") == categ ):
            activosCate.append({ 
            "Codigo de Campus": val.get("CodCampus"),
            "Nombre": val.get("Nombre"),
            "Numero del Serial" : val.get("NroSerial")
            })
    return activosCate

#Listar Activos Dados De Baja Por Daño 
def getActivosDaño():
    activos = getAllDataActivos()
    
    activosDaño = []  # Lista para almacenar activos con estado igual a "2"
    for val in activos:
        if val.get("idEstado") == "2":  # Accede correctamente a "idEstado"
            activosDaño.append(val)  # Agrega el activo a la lista
    return activosDaño


#Debemos enlistar todos los activos con su asignación
def getActiAsig():
    ACTIVOasignado = []
    activos = getAllDataActivos()
    for val in activos:
        if val.get("idEstado") == "1":
            Nombre = val.get("Nombre")
            id = val.get("id")
            asignado = val.get("asignaciones", [])  
            ACTIVOasignado.append((Nombre, id, asignado))

    return ACTIVOasignado 

#Necesitamos el historial de todo un  activo (incluyendo sus asignaciones y bajas por daño).
def getHistorial(id):

    for val in getAllDataActivos():
        if val.get("id") == id :
            historial = val.get("historialActivos")             
            return historial

        

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
              
                +-+-+-+-+ +-+ +-+-+-+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+
                |M|E|N|U| |-| |M|O|V|I|M|I|E|N|T|O| |D|E| |A|C|T|I|V|O|S|
                +-+-+-+-+ +-+ +-+-+-+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+

              
            OPCIONES 
                1. RETORNO DE ACTIVO
                2. DAR DE BAJA ACTIVO
                3. CAMBIAR ASIGNACION DE ACTIVO
                4. ENVIAR A GARANTIA ACTIVO
                5. REGRESAR AL MENU PRINCIPAL

              """)
        
        opcion = input("\nSeleccione una de las opciones: ")
        #Pedimos al usuario ingresar un número para escoger la opción que desea del menú de MOVIMIENTO DE ACTIVOS.
        if re.match(r'^[1-5]$', opcion) is not None:
            #Con esta validación vamos a comprobar que el número que ingrese se encuentre
            #Dentro del parametro de 1 a 7. Además, de que en caso de que ingrese un 
            #número distinto a los posibles, volvera a sacar el mismo menú.
            opcion = int(opcion)  # Lo convertimos a un número entero
            #Empezamos a meter los condicionales para el menú.
        if (opcion == 1):
            print(tabulate(getAllActivosCODCAMPUS(), headers = "keys", tablefmt="rounded_grid"))
            #RETORNO DE ACTIVO
        elif (opcion == 2):
            print(tabulate((),headers= "keys", tablefmt="rounded_grid"))
            #DAR DE BAJA ACTIVO
        elif (opcion == 3):
            print(tabulate((),headers= "keys", tablefmt="rounded_grid"))
            #CAMBIAR ASIGNACION DE ACTIVO
        elif (opcion == 4):
            print(tabulate((),headers= "keys", tablefmt="rounded_grid"))
            #ENVIAR A GARANTIA ACTIVO
        elif(opcion == 5):
            break
        #Volver al menú principal