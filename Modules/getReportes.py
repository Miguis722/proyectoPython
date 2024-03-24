import os
import re
import requests
from tabulate import tabulate
import json


#Servidor de Reportes
def getAllDataReportes():
	peticion = requests.get("http://154.38.171.54:5502/activos")
	data = peticion.json()
	return data

#Hacemos el primer filtro que se nos pide, el cual es el de listar todos los activos. Le ponemos un diseño en especial para que aparezca de forma bonita, clara
#Y legible, facil de entender.
def getAllDataReportesOrganizado():
    DataReportesOrganized = list()
    for val in getAllDataReportes():
          #Recordar que si dejamos los nombres como están se pueden mezclar con otros reportes y generarn errores.
          #Además que los nombres de las variables DEBEN tener un "_" porque sino no funcionaran.
        externocleidomastoideo = dict({
            "Identificacion": val.get('NroItem'),
            "CodigoTransacción": val.get('CodTransaccion'),
            "Serial": val.get('NroSerial'),
            "CodigoCampus": val.get('CodCampus'),
            "Formulario": val.get('NroFormulario'),
            "Nombre": val.get('Nombre'),
            "Proveedor": val.get('Proveedor'),
            "Responsable": val.get('EmpresaResponsable'),
            "Id de la marca": val.get('idMarca'),
            "Id de la categoria": val.get('idCategoria'),
            "Id del tipo": val.get('idTipo'),
            "Precio": val.get('ValorUnitario'),
            "Estado": val.get('idEstado'),
            "Identificador": val.get('id'),
            "Asignación": val.get('asignaciones')
        })        
        DataReportesOrganized.append(externocleidomastoideo)
    return DataReportesOrganized
#Recordemos cambiar el nombre con el que se mostrara al usuario, para que asi el usuario no sepa el
#Orden y nombre de como tenemos organizado la base de datos.


def menu():
    while True:
        #CLS se usa en vez del CLEAR, debido a que uso Windows y no Linux.
        os.system("cls")
        print("""

                +-+-+-+-+ +-+ +-+-+-+-+-+-+-+-+
                |M|E|N|U| |-| |R|E|P|O|R|T|E|S|
                +-+-+-+-+ +-+ +-+-+-+-+-+-+-+-+

              
            OPCIONES 
                1. LISTAR TODOS LOS ACTIVOS
                2. LISTAR ACTIVOS POR CATEGORIA
                3. LISTAR ACTIVOS DADOS POR BAJA POR DAÑO
                4. LISTAR ACTIVOS Y ASIGNACION
                5. LISTAR HISTORIAL DE MOV. DE ACTIVO
                6. REGRESAR AL MENU PRINCIPAL

              """)
        
        opcion = input("\nSeleccione una de las opciones: ")
        #Pedimos al usuario ingresar un número para escoger la opción que desea del menú de REPORTES

        if re.match(r'^[1-6]$', opcion) is not None:
            #Con esta validación vamos a comprobar que el número que ingrese se encuentre
            #Dentro del parametro de 1 a 7. Además, de que en caso de que ingrese un 
            #número distinto a los posibles, volvera a sacar el mismo menú.

            opcion = int(opcion)  # Lo convertimos a un número entero

            #Empezamos a meter los condicionales para el menú.

        #Si la opción del usuario es 1, entonces mostrara una lista con todos los activos
        if (opcion == 1):
            print(tabulate(getAllDataReportesOrganizado(),headers="keys", tablefmt = "rounded_grid"))
            input("Presione 0 (Cero) para volver: ")#Ponemos un input para que cuando corramos lo que necesitamos no se borre lo que queremos mostrar.
        #LISTAR TODOS LOS ACTIVOS

        #elif (opcion == 2):
            #LISTAR ACTIVOS POR CATEGORIA

        #elif (opcion == 3):
            #LISTAR ACTIVOS DADOS POR BAJA POR DAÑO

        #elif (opcion == 4):
            #LISTAR ACTIVOS Y ASIGNACION

        #elif (opcion == 5):
            #LISTAR HISTORIAL DE MOV. DE ACTIVO

        elif (opcion == 6):
            break
        #Volver al menú principal