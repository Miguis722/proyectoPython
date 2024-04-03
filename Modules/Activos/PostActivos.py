from tabulate import tabulate
import os
import re
import json
import requests

#Servidor de Activos
def getAllDataActivos():
	peticion = requests.get("http://154.38.171.54:5501/activos")
	data = peticion.json()
	return data

#Queremos obtener solamente el NroItem
def ActivosNroItem(NroItem):
    for val in getAllDataActivos():
        if val.get('NroItem') == NroItem:
            return [val]


# Aquí se crea una lista de todos los NroItem existentes y se devuelve el siguiente número disponible.
# Es decir, que aqui se hara que cuando agreguemos a un nuevo activo, se agregue un NroItem, y se le agregue un nuevo NroItem, si por ejemplo hay 99
# Entonces nos dara ese número y se le agregara un uno dandonos un nuevo NroItem llamado 100.

def nuevoInfoActivos():
    NroItem = []
    for val in getAllDataActivos():
        NroItem.append(val.get('NroItem'))
    if NroItem:
        return max(NroItem) + 1
    else:
        return 1


#Deseamos agregar la información de un nuevo Activo, asignandole automaticamente un nuevo número de NroItem
def AddInfoActivos():
    Activo = {}
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            if not Activo.get('NroItem'):
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    NumeroItem = input('Ingrese el número de item del activo:')
                    if NumeroItem.isdigit():
                        NumeroItem = int(NumeroItem)
                        data = ActivosNroItem(NumeroItem)
                        if data:
                            raise Exception('El número de item del activo introducido ya existe, porfavor verifique.')
                        else:
                            Activo['NroItem'] = NumeroItem
                    else:
                        raise Exception('El número de item del activo no cumple con el patrón establecido, porfavor verifique.')
                    break
            
            if not Activo.get('CodTransaccion'):
                CodTransaccion = input('Ingrese el código de transacción del activo: ')
                if CodTransaccion.isdigit():
                    CodTransaccion = int(CodTransaccion)
                    Activo['CodTransaccion'] = CodTransaccion
                else:
                    raise Exception('El código de transacción del activo solo puede tener dígitos numéricos.')

            if not Activo.get("Nroserial"):
                print(""" 
                    ¿El activo posee un número de serial?
                        1. Si
                        2. No
                """)
                opcion = input("\nSeleccione una opción: ")
                if re.match(r'^[1-2]$', opcion):
                    if opcion == '1':
                        Nroserial = input("Ingrese el Serial del activo: ")
                        if re.match(r'^[A-Za-z0-9]+$', Nroserial):
                            Activo["Nroserial"] = Nroserial
                        else:
                            raise Exception ("El Serial ingresado no cumple con los parámetros establecidos, por favor verifique.")
                    else:
                        Activo["Nroserial"] = 'Sin Serial'

            if not Activo.get("CodCampus"):
                CodCampus = input("Ingrese el Codigo en Campus: ")
                if re.match(r'[A-Za-z]{3}\d{3}', CodCampus):
                    Activo["CodCampus"] = CodCampus
                else:
                    raise Exception ("El Codigo en Campus ingresado no cumple con los parametros establecidos, por favor verifique.")

            if not Activo.get("NroFormulario"):
                NroFormulario = input("Ingrese el Numero de formulario del activo: ")
                if re.match(r'^[0-9]+$', NroFormulario):
                    Activo["NroFormulario"] = int(NroFormulario)
                else:
                    raise Exception ("El número de formulario del activo ingresado no cumple con los parámetros establecidos, por favor verifique.")

            if not Activo.get("Nombre"):
                Nombre = input("Ingrese el Nombre del Activo, tome de ejemplo (Ejemplo-12345678-ABC-1234): ")
                if re.match(r'^[a-zA-Z]+-[^\s]{8}-[^\s]{3}-[^\s]{4}\s*$', Nombre):
                    Activo["Nombre"] = Nombre
                else:
                    raise Exception ("El Nombre del activo ingresado no cumple con los parametros establecidos, por favor verifique.")

            if not Activo.get("Proveedor"):
                Proveedor = input("Ingrese el nombre del Proveedor del Activo: ")
                if re.match(r'^[A-Z][a-záéíóúñ]+(?:\s+[A-Z][a-záéíóúñ]+)*$', Proveedor):
                    Activo["Proveedor"] = Proveedor
                else:
                    raise Exception ("El Proveedor del activo ingresado no cumple con los parametros establecidos, por favor verifique.")

            if not Activo.get("EmpresaResponsable"):
                EmpresaResponsable = input("Ingrese la Empresa Responsable del Activo: ")
                if re.match(r'^[A-Z][a-záéíóúñ]+(?:\s+[A-Z][a-záéíóúñ]+)*$', EmpresaResponsable):
                    Activo["EmpresaResponsable"] = EmpresaResponsable
                else:
                    raise Exception ("La empresa Responsable del activo ingresado no cumple con los parametros establecidos, por favor verifique.")

            print("""Las marcas disponibles son:
                1. lg
                2. compumax
                3. logitech
                4. benq
                5. asus
                6. lenovo
                7. hp
            """)
            idMarca = input("Ingrese el número id de la Marca: ")
            if re.match(r'^[1-7]$', idMarca):
                Activo["idMarca"] = idMarca
            else:
                raise Exception ("El número id de la Marca ingresado no cumple con los parametros establecidos, por favor verifique.")

            print("""
                Las categorias disponibles son:                      
                1. equipo de computo
                2. electrodomestico
                3. juego
            """)
            idCategoria = input("Ingrese el ID de la Categoria: ")
            if re.match(r'^[1-3]$', idCategoria):
                Activo["idCategoria"] = idCategoria
            else:
                raise Exception ("El ID de la Categoria ingresado no cumple con los parametros establecidos, porfavor verifiquelo.")

            print("""Los tipos de activo disponibles son:
                1. monitor
                2. cpu
                3. teclado
                4. mouse
                5. aire acondicionado
                6. portatil
                7. televisor
                8. Arcade
            """)
            idTipo = input("Ingrese ID del tipo de Activo: ")
            if re.match(r'^[1-8]$', idTipo):
                Activo["idTipo"] = idTipo
            else:
                raise Exception ("El ID del Tipo de Activo ingresado no cumple con los parametros establecidos, porfavor verifique.")

            ValorUnitario = input("Ingrese el Valor del Activo (c/u): ")
            if re.match(r"^[0-9]+$", ValorUnitario):
                Activo["ValorUnitario"] = ValorUnitario
            else:
                raise Exception ("El valor del activo ingresado no cumple con los parametros establecidos, porfavor verifique.")

            print("""
                Los estados disponibles son:
                0. No asignado
                1. asignado
                2. dado de baja por daño
                3. en reparación y/o garantia
            """)
            idEstado = input("Ingrese el ID del estado del activo: ")
            if re.match(r"^[0-9]+$", idEstado):
                Activo["idEstado"] = int(idEstado)
            else:
                raise Exception ("El ID del estado del activo ingresado no cumple con los parametros establecidos, porfavor verifique.")

            raise Exception("Se ha creado el Activo deseado.")
    except Exception as error:
        print(error)

        headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
        peticion = requests.post("http://154.38.171.54:5501/activos", headers=headers, data=json.dumps(Activo, indent=4))
        res = peticion.json()
        return [res]


                











     

def menu():
    while True:
        #CLS se usa en vez del CLEAR, debido a que uso Windows y no Linux.
        os.system('cls' if os.name == 'nt' else 'clear')
        #Link para sacar el diseño:
        # https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Digital&t=AGREGAR%20ACTIVOS
        print("""
                
                    +-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+
                    |A|G|R|E|G|A|R| |A|C|T|I|V|O|S|
                    +-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+

                            
            OPCIONES 
                0. Si desea volver atrás.
                1. Para continuar
                

              """)
        
        opcion = input("\nSeleccione una de las opciones: ")
        #Pedimos al usuario ingresar un número para escoger la opción que desea del menú de ACTIVOS
        if re.match(r'^[0-1]$', opcion) is not None:
            #Con esta validación vamos a comprobar que el número que ingrese se encuentre
            #Dentro del parametro de 1 a 7. Además, de que en caso de que ingrese un 
            #número distinto a los posibles, volvera a sacar el mismo menú.
            opcion = int(opcion)  # Lo convertimos a un número entero
            #Empezamos a meter los condicionales para el menú.
        if (opcion == 0):
            break
            #Volver al menú principal
        
        elif (opcion == 1):
            print(tabulate(AddInfoActivos()))
            input("Presione 0 (Cero) para volver: ")  # Ponemos un input para que cuando corramos lo que necesitamos no se borre lo que queremos mostrar.
            #Agregar
       