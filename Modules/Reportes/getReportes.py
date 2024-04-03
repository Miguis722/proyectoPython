import os
import re
import requests
from tabulate import tabulate
import json

#Servidor de Categorias
def getAllDataCategorias():
    peticion = requests.get("http://154.38.171.54:5503/categoriaActivos")
    data = peticion.json()
    return data

#codigo1 = "Equipo de Computo"
#codigo2 = "Electrodomestico"
#codigo3 = "Juego"

#Servidor de Reportes
def getAllDataReportes():
	peticion = requests.get("http://154.38.171.54:5503/activos")
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

#Queremos filtrar los diferentes ACTIVOS por las diferentes CATEGORIAS disponibles (1, 2 y 3).
#¿Que categoria hay disponibles por el momento? 
                #1. Equipo de Computo
                #2. Electrodomesticos
                #3. Juego
def getAllActivosXCategoria(idCategoria):
    CategoriasDisponibles = []
    for val in getAllDataReportes():
        if idCategoria == val.get('idCategoria'):
            #Si escoge una opcion que se encuentra dentro de los parametros, entonces se mostrara, sino, no.
                    CategoriasDisponibles.append({
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
                        "Id del tipo": val.get('idTipo'),
                        "Precio": val.get('ValorUnitario'),
                        "Estado": val.get('idEstado'),
                        "Identificador": val.get('id')
                        #"Asignación": val.get('asignaciones'), 
                                       
                    })

    return CategoriasDisponibles
                  
#Queremos filtrar los diferentes ACTIVOS que se han dado de BAJA POR DAÑO.
#Estados:
        # 0. No asignado.
        # 1. Asignado.
        # 2. Dado de baja por daño.
        # 3. En reparación y/o garantia.
def getAllActivosDadosDeBajaPorDaño():
    ActivosDañados = []
    for val in getAllDataReportes():
          if val.get( 'idEstado' ) == "2": 

            ActivosDañados.append({ 
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
                        "Id del tipo": val.get('idTipo'),
                        "Precio": val.get('ValorUnitario'),
                        "Identificador": val.get('id')
            })
    return  ActivosDañados

#Queremos filtrar los diferentes ACTIVOS que se encuentren ASIGNADOS
def getAllActivosAsignados():
    ActivosAsignados = []
    for val in getAllDataReportes():
        if val.get('idEstado') == "1":
               ActivosAsignados.append({ 
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
                        "Id del tipo": val.get('idTipo'),
                        "Asignado a": val.get('asignaciones')
                })
    return ActivosAsignados

#Queremos hacer un filtro el cual se nos muestre TODOS los movimientos que ha tenido un activo.
def getAllTrayectoriaDeActivos():
    Trayectoria = []
    for val in  getAllDataReportes():
        Trayectoria.append({
            "Identificacion": val.get('NroItem'),
            "Item N°" : val.get("NroItem"),  
            "Número de serie": val.get("NroSerial"),
            "Nombre": val.get('Nombre'),
            "Proveedor": val.get('Proveedor'),
            "Responsable": val.get('EmpresaResponsable'),
            "Id de la marca": val.get('idMarca'),
            "Id del tipo": val.get('idTipo'),
            "Historial": val.get('historialActivos')
        })
    return Trayectoria


def menu():
    while True:
        #CLS se usa en vez del CLEAR, debido a que uso Windows y no Linux.
        os.system('cls' if os.name == 'nt' else 'clear')
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

        #Si la opción del usuario es 2, entonces mostrara una lista  con los activos por categoría.
        elif (opcion == 2):
            print("""  ¿Que categoria deseas visualizar? 
                  
                            1. Equipo de Computo
                            2. Electrodomesticos
                            3. Juego""")
            
            idCategoria = input("\nCategoria Deseada: ")
            if re.match(r'^[1-3]$', idCategoria) is not None:
                idCategoria = (idCategoria) 
            
            print(tabulate(getAllActivosXCategoria(idCategoria),headers="keys", tablefmt = "rounded_grid"))
            input("Presione 0 (Cero) para volver: ")#Ponemos un input para que cuando corramos lo que necesitamos no se borre lo que queremos mostrar.
        #LISTAR ACTIVOS POR CATEGORIA
            
        #Si la opción del usuario es 3, entonces mostrara una lista con los activos que han sido de baja por daño.
        elif (opcion == 3):
            print(tabulate(getAllActivosDadosDeBajaPorDaño(),headers="keys", tablefmt = "rounded_grid"))
            input("Presione 0 (Cero) para volver: ")#Ponemos un input para que cuando corramos lo que necesitamos no se borre lo que queremos mostrar.
        #LISTAR ACTIVOS DADOS POR BAJA POR DAÑO
            
        #Si la opción del usuario es 4, entonces mostrara una lista con todos los activos que se encuentren asignados.
        elif (opcion == 4):
            print(tabulate(getAllActivosAsignados(),headers="keys", tablefmt = "rounded_grid"))
            input("Presione 0 (Cero) para volver: ")#Ponemos un input para que cuando corramos lo que necesitamos no se borre lo que queremos mostrar.
        #LISTAR ACTIVOS Y ASIGNACION
        
        #Si la opción del usuario es 5, entonces mostrara una lista con todos el historial que ha tenido un activo.
        elif (opcion == 5):
            print(tabulate(getAllTrayectoriaDeActivos(),headers="keys", tablefmt = "rounded_grid"))
            input("Presione 0 (Cero) para volver: ")#Ponemos un input para que cuando corramos lo que necesitamos no se borre lo que queremos mostrar.
        #LISTAR HISTORIAL DE MOV. DE ACTIVO
            
        #Si se escoge 6, entonces volvera al menú principal.
        elif (opcion == 6):
            break
        #Volver al menú principal