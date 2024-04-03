from tabulate import tabulate
import os
import re
import json
import requests
import datetime
import uuid

#Servidor de Activos
def getAllDataActivos():
	peticion = requests.get("http://154.38.171.54:5502/activos")
	data = peticion.json()
	return data

def ActivoPorid(id):
    for acito in getAllDataActivos():
        if acito.get('id') == id:
            return acito
        else:
            print('\nEl activo no existe')
            return None


def deleteActivos(ID):
    try:
    # Obtiene los datos del personal con el ID proporcionado
        data = ActivoPorid(ID)
        # Verifica si el activo tiene asignaciones
        if data["asignaciones"] == []:
            data["idEstado"] = "2"
            historial = {}
            if not historial.get("NroId"):
                historial["NroId"] =str(uuid.uuid4().hex[:4])
            if not historial.get("Fecha"):
                fechaactual = datetime.datetime.now().strftime('%Y/%m/%d')
                historial["Fecha"] = fechaactual
            if not historial.get("tipoMov"):
                historial["tipoMov"] = "2" 
            data.setdefault("historialActivos", []).append(historial)
            url = (f"http://154.38.171.54:5502/activos{ID}")
            peticion = requests.put(url, data=json.dumps(data, indent=4).encode("UTF-8"))
            res = peticion.json()
            res["Mensaje"] = "El Activo que deseaba, ha sido modificado con exito."
            raise Exception("Ha ocurrido un error modificando el estado.")
    except Exception as error:
        print(error)
                


    # Espera la entrada del usuario para volver
    input("Presione Enter para volver: ")

#Hacemos el Menú
def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        #Link para sacar el diseño:
        # https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Digital&t=AGREGAR%20ACTIVOS
        print("""
              
              
                +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+
                |E|L|I|M|I|N|A|R| |A|C|T|I|V|O|S|
                +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+

               0. Si desea voler atrás.
               1. Para continuar.
               
               """)
        opcion = input("\nSeleccione una de las opciones: ")
        # Pedimos al usuario ingresar un número para escoger la opción que desea del menú de ELIMINAR ACTIVOS
        if re.match(r'^[0-1]$', opcion) is not None:
        # Con esta validación vamos a comprobar que el número que ingrese se encuentre
        # Dentro del parámetro de 0 a 1. Además, de que en caso de que ingrese un
        # número distinto a los posibles, volverá a sacar el mismo menú.
            opcion = int(opcion)  # Lo convertimos a un número entero
        # Empezamos a meter los condicionales para el menú.
        # Si la opción es cero, va al menú anterior (getActivos).
        if opcion == 0:
            break
            
        # Si el usuario selecciona 1, modificara/editara los datos.
        elif opcion == 1:
            ID = input("Ingrese el ID que desea eliminar: ")
            print(tabulate(deleteActivos(ID)), headers="keys", tablefmt="rounded_grid")
            input("Presione 0 (Cero) para volver: ")  # Ponemos un input para que cuando corramos lo que necesitamos no se borre lo que queremos mostrar.
        #Eliminar