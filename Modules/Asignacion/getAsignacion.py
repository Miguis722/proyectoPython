import os
import re
import requests
import json
from datetime import date as fecha_hoy
from tabulate import tabulate

def obtener_todos_los_activos():
    peticion = requests.get("http://154.38.171.54:5501/activos")
    datos = peticion.json()
    return datos

def obtener_activo_por_id(id_activo):
    for valor in obtener_todos_los_activos():  
        if valor.get("id") == id_activo:  
            return valor  

def obtener_nombres_y_ids_personas():
    nombres_personas = []
    for val in obtener_todos_los_activos():
        nombre = val.get("Nombre")
        id_persona = val.get("id")
        nombres_personas.append((nombre, id_persona))
    return nombres_personas

def obtener_nombres_y_ids_zonas():
    nombres_zonas = []
    for val in obtener_todos_los_activos():
        nombre_zona = val.get("nombreZona")
        id_zona = val.get("id")
        nombres_zonas.append((nombre_zona, id_zona))
    return nombres_zonas

def obtener_asignacion_por_numero(num_asignacion):
    activos = obtener_todos_los_activos() 
    
    for val in activos:
        asignaciones = val.get("asignaciones", [])
        for val in asignaciones:
            if val.get("NroAsignacion") == num_asignacion:
                return [val]  

def asignar_activo(id_activo):
    activo = obtener_activo_por_id(id_activo)
    
    if activo:  
        while True:
            if activo["idEstado"] != "0": 
                print("Este activo ya tiene asignación, no se puede volver a asignar.")
                break
            else:
                try:
                    activo["idEstado"] = "1" 

                    num_asignacion = input("Ingrese un numero para la asignacion: ")
                    if re.match(r'^[0-9]+$', num_asignacion):
                        num_asignacion = str(num_asignacion)
                    else:
                        raise Exception("El numero ingresado no cumple con el estandar, intentelo denuevo")
                    
                    fecha_asignacion = str(fecha_hoy())

                    tipo_asignacion = input("Ingrese el Tipo de Asignacion (Personal / Zona): ")
                    if re.match(r'^(Personal|Zona)$', tipo_asignacion ):
                        tipo_asignacion = tipo_asignacion
                    else:
                        raise Exception("Asignacion no válida. Por favor, ingrese 'Personal' o 'Zona', empezando con Mayuscula.") 

                    if (tipo_asignacion == "Personal"):
                        asignado_a =  input("Ingrese id de la Persona a la que desea asignar:\n" + "".join([f"\t{i}. {val}\n" for i, val in enumerate(obtener_nombres_y_ids_personas())]))
                        if(re.match(r'^[0-9]+$', asignado_a)):
                            asignado_a = str(asignado_a)
                    
                    elif (tipo_asignacion == "Zona"):
                        asignado_a =  input("Ingrese el id de la Zona a la que desea asignar:\n" + "".join([f"\t{i}. {val}\n" for i, val in enumerate(obtener_nombres_y_ids_zonas())]))
                        if(re.match(r'^[0-9]+$', asignado_a)):
                            asignado_a = str(asignado_a)

                    activo["asignaciones"] = [
                        {
                            "NroAsignacion": num_asignacion,
                            "FechaAsignacion": fecha_asignacion,
                            "TipoAsignacion": tipo_asignacion,
                            "AsignadoA": asignado_a
                        }
                    ]
                    id_historial = "1"
                    movimiento_activo = activo["idEstado"]
                    activo["historialActivos"] = [            
                        {
                            "NroId": id_historial,
                            "Fecha": fecha_asignacion,
                            "tipoMov": movimiento_activo,
                            "idRespMov": "6ee3"
                        }
                    ]

                    peticion = requests.put(f"http://154.38.171.54:5501/activos/{id_activo}", data=json.dumps(activo))
                    if(peticion.status_code == 200):
                        return print("La asignacion ha sido realizada correctamente")
                    break  
                except Exception as error:
                    print('-ERROR-')
                    print(error)
            break                
    else:
        print(f"El activo con el ID: {id_activo} no existe, por favor intetelo denuevo") 
        return None



def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
            
                +-+-+-+-+ +-+ +-+-+-+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+
                |M|E|N|U| |-| |A|S|I|G|N|A|C|I|O|N| |D|E| |A|C|T|I|V|O|S|
                +-+-+-+-+ +-+ +-+-+-+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+


            OPCIONES 
                1. CREAR ASIGNACION
                2. BUSCAR ASIGNACION
                3. REGRESAR AL MENU PRINCIPAL

              """)
        
        opcion = input("\nSeleccione una de las opciones: ")
        #Pedimos al usuario ingresar un número para escoger la opción que desea del menú de ASIGNACION
        if re.match(r'^[1-3]$', opcion) is not None:
            #Con esta validación vamos a comprobar que el número que ingrese se encuentre
            #Dentro del parametro de 1 a 7. Además, de que en caso de que ingrese un 
            #número distinto a los posibles, volvera a sacar el mismo menú.
            opcion = int(opcion)  # Lo convertimos a un número entero
            #Empezamos a meter los condicionales para el menú.
        if (opcion == 1):
            idActivo = (input("Ingrese el id del Activo a asignar: "))
            print(tabulate(asignar_activo(idActivo), headers = "keys", tablefmt="rounded_grid"))
            #CREAR ASIGNACIÓN
        elif (opcion == 2):
            NumerodeAsig = input("Ingrese el número de la asignacion: ")
            print(tabulate(obtener_asignacion_por_numero(NumerodeAsig), headers = "keys", tablefmt="rounded_grid"))
            #BUSCAR ASIGNACIÓN
        elif (opcion == 3):
            break
        #Volver al menú principal