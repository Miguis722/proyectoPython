from tabulate import tabulate
import os
import re
import requests
import json
import getActivos as GetActivos
#Servidor de Activos
def getAllDataActivos():
	peticion = requests.get("http://154.38.171.54:5502/activos")
	data= peticion.json()
	return data

#Para hacernos la vida más facil, y no mostrar un número en vez de la marca
# haré una función que se encargue de mostrar en vez de los números.
# El primer paso será traer todas las marcas.

def MarcasExistentes():
    peticion = requests.get("http://154.38.171.54:5502/marcas")
    data = peticion.json()

    #Aqui estamos creando un diccionalio en el cual se guardaran las marcas con sus respectivos id's.
    marcas = {}
    for marca in data:
        marcas[marca['Nombre']] = marca['id']
    return marcas

# El segundo paso será que si existe esa marca, buscara el ID.
#Esta función busca el número de identificación (ID) de una marca dado su nombre.
def NumeroDeMarcaExistenteXMarca(nombre_marca):
    marcas = MarcasExistentes()
    return marcas.get(nombre_marca, "Marca no encontrada")



#Deseamos editar un dato de los ya existentes en la base de datos.
def updateActivos(id):
    data = getAllDataActivos(id)
    if(len(data)):
        print("Activo Encontrado")
        print(tabulate([data], headers="keys", tablefmt="rounded_grid"))
        data["NroItem"] = data["NroItem"]
        continuarActualizar = True
        while continuarActualizar:
            try:

                print("""
                      
                        ¿Que dato deseas cambiar?

                    0. Volver atrás.
                                            
                    1. Serial
                    2. Codigo en Campus
                    3. Número de Formulario
                    4. Nombre
                    5. Proveedor
                    6. Empresa Responsable
                    7. Marca
                    8. Categoria
                    9. Precio Unidad
                    10. Estado
                    
                """)

                opcion = input("\nSeleccione una de las opciones: ")
                if re.match(r'[0-10]$', opcion) is not None:
                    opcion = int(opcion)

                    #Si el usuario escoge el número cero (0), lo devolvera al menú. Pensando en que la persona puede que se equivocara y desee volver al menú.
                    if(opcion == 0):
                            break
                    
                    #Si el usuario escoge el número uno (1), modificara el Serial.
                    elif(opcion == 1):
                            while True:
                                try:
                                    Serial = input("Ingrese el Serial: ")
                                    #Permite ingresar letras mayúsculas y minúsculas. Además de que puede ingresar números del 0 al 9.
                                    if re.match(r'[A-Za-z0-9]+', Serial) is not None:

                                        #Acepta cualquier combinación de letras y números en cualquier orden y en cualquier cantidad.
                                        #Es decir que si por ejemplo ponemos un 123HolaMundo, lo aceptara, al igual que un Hola123Mundo.
                                        #Ya que no importa el Orden que tenga.

                                        data["NroSerial"] = Serial
                                        break
                                    else:
                                        #Si se llegasen a agregar caracteres especiales, ahi si no cumpliria con el patrón ya dado, se lanza una excepción con un mensaje de error explicando que el código de Serial no cumple con los requisitos establecidos.
                                        #Por ejemplo: "!@#$%^&*()" No cumplirian con el patrón.
                                        raise Exception("El serial no cumple con el patrón establecido.")  
                                except Exception as error:
                                    print(error)

                    #Si el usuario escoge el número dos (2), modificara el  Código en Campus.
                    elif(opcion == 2):
                            while True:
                                try:
                                    CodCampus = input("Ingrese el Codigo en Campus, utilice como ejemplo (HOL123): ")
                                    if re.match(r'[A-Za-z]{3}\d{3}', CodCampus) is not None:

                                        # A-Z haria que se puedan meter letras desde la A a la Z en mayusculas y luego el a-z haria que se puedan escribir en minusculas.
                                        #re.match(r'[A-Za-z]{3}\d{3}',
                                        #Haria que  la cadena solo contuviera letras y numeros, pero no espacios.
                                        #Y que tuviera un orden de HOL123

                                        data["CodCampus"] = CodCampus
                                        break
                                    else:
                                        #Si se llegasen a poner caracteres especiales, o un patrón diferente al puesto.
                                        #Por ejemplo: 123HOL no cumpliria con el patrón impuesto/establecido.
                                        raise Exception("El codigo en Campus no cumple con el patrón establecido.")
                                except Exception as error:
                                    print(error)

                    #Si el usuario escoge el número tres (3), modificara el Número de Formulario
                                    #El número de digitos en este es de nueve (9)
                    elif(opcion == 3):
                            while True:
                                try:
                                    NroFormulario = input("Ingrese el número de Formulario del activo: ")
                                    if(re.match(r'[0-9]{9}', NroFormulario) is not None):

                                        #Estamos pidiendo  al usuario una cantidad de numeros exactos, el cual es de 9, ya que el patrón que se usa
                                        #Es de maximo 9 digitos, además estamos poniendo de condición que los números que ingrese deben estar dentro de los parametros 0-9.

                                        data["NroFormulario"] = NroFormulario
                                        break
                                    else:
                                        #Si se llegase a poner una letra, o un caracter especial
                                        #Se mostraría este mensaje y volveria al inicio del bucle while.
                                        raise Exception("El número de formulario no cumple con el patrón establecido.") 
                                except Exception as error:
                                    print(error)

                    #Si el usuario escoge el número cuatro (4), modificara el Nombre
                    elif(opcion == 4):
                            while True:
                                try:
                                    Nombre = input("Ingrese el Nombre del activo, utilice como ejemplo (Ejemplo-12345678-ABC-1234): ")
                                    #^[^\d\s] Hace que los  nombres puedan tener hasta 8 digitos pero que no se agregue algún número
                                    #Porque puede que escriban CPU1234, entonces para evitar esto ponemos un condicional de que solo se puedan 
                                    #Poner letras.
                                    #Cualquier carácter que no sea un guion o un espacio en blanco, al menos una vez.
                                    #Esto permitirá que haya cualquier cantidad de caracteres antes del primer guion
                                    if (r'^[a-zA-Z]+-[^\s]{8}-[^\s]{3}-[^\s]{4}\s*$', Nombre) is not None:
                                        Nombre = (Nombre)
                                        data["Nombre"] = Nombre
                                        break
                                    else:
                                        raise Exception("El Nombre del activo no cumple con el patrón establecido.")   
                                except Exception as error:
                                    print(error)
                                                                                                  
                    #Si el usuario escoge el número cinco (5), modificara al Proveedor.
                    elif(opcion == 5):
                         while True:
                            try:
                                Proveedor = input("Ingrese el Nombre del Proovedor del activo: ")

                                #'^[a-zA-Z]$' Esto nos estaria permitiendo nada más poder ingresar letras, sin una cantidad especifica.
                                # Si agregamos una + antes del $, significa que podremos agregar más de un caracter.                                                            
                                if (r'^[a-zA-Z]+$', Proveedor) is not None:
                                        data["Proveedor"] = Proveedor
                                        break
                                else:
                                        raise Exception("El Nombre del Proovedor no cumple con el patrón establecido.")   
                            except Exception as error:
                                print(error)

                #Si el usuario escoge el número seis (6), modificara a la empresa Responsable
                elif(opcion == 6):
                    while True:
                        try:
                              NombreEmpresaResponsable = input("Ingrese el Nombre de la empresa Responsable: ")

                              if (r'^[a-zA-Z]+$', NombreEmpresaResponsable) is not None:
                                        data["EmpresaResponsable"] = NombreEmpresaResponsable
                                        break
                              else:
                                   raise Exception("El Nombre de la Empresa Responsable no cumple con el patrón establecido.")
                        except Exception as error:
                            print(error)
#Ya van 6, faltan 4 más. 

                #Si el usuario escoge el número siete (7), modificara la marca.

                # elif opcion == 7:
                #     while True:
                #          try:
                #               Marca = input("Ingrese el Nombre de la marca.")
                #                 if (r'^[a-zA-Z]+$', Marca) is not None:
                #                         data["EmpresaResponsable"] = Marca
                #                         break
                #               else:
                #                    raise Exception("El Nombre de la Empresa Responsable no cumple con el patrón establecido.")
                #         except Exception as error:
                #             print(error)

                    #Es en cuyo caso se desee EDITAR más de un dato (por ejemplo, que ya editamos un dato y queramos cambiar otro sin tener que buscar TODO de vuelta.)
                    confirmacion = ""            
                    while (confirmacion !=  "s" and confirmacion != "n"):
                            confirmacion = input("Deseas cambiar más datos?(s/n): ")
                            if re.match(r'^[sn]$',confirmacion):
                                if confirmacion == "n":
                                    continuarActualizar = False
                                    break
                                else:
                                    confirmacion == "s"
                                    break
                            else:
                                print("La confirmación no cumple con lo establecido. Por favor, solo utilice: s / n")
            except Exception as error:
                print(error)
        
        headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
        peticion = requests.put(f"http://154.38.171.54:5502/activos?NroItem", headers="keys", data=json.dumps(data))
        res = peticion.json()
        return [res]
    else:
        return[{
            "Mensaje": "Activo no encontrado"
        }]





def menu():
	while True:
		os.system("cls")
		print("""


 ____ ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ 
||E |||D |||I |||T |||A |||R |||       |||A |||C |||T |||I |||V |||O |||S ||
||__|||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|

		
		0. Si desea volver atrás.
		1. Para continuar.

""")
opcion = input("Seleccione una de las opciones: ")
# Pedimos al usuario ingresar un número para escoger la opción que desea del menú de EDITAR ACTIVOS
if re.match(r'^[0-1]$', opcion) is not None:
    # Con esta validación vamos a comprobar que el número que ingrese se encuentre
    # Dentro del parámetro de 0 a 1. Además, de que en caso de que ingrese un
    # número distinto a los posibles, volverá a sacar el mismo menú.
    opcion = int(opcion)  # Lo convertimos a un número entero
    # Empezamos a meter los condicionales para el menú.
    # Si la opción es cero, va al menú anterior (getActivos).
    if opcion == 0:
        GetActivos.menu()
        # al usar el codigo de break para poder volver al menú de getActivos daba error, por lo que
        # Para solucionarlo y no quedarme sin opciones, decidi importar getActivos
        
    # Si el usuario selecciona 1, modificara/editara los datos.
    elif opcion == 1:
        print(tabulate(updateActivos(id)))
        input("Presione 0 (Cero) para volver: ")  # Ponemos un input para que cuando corramos lo que necesitamos no se borre lo que queremos mostrar.
    # Editar