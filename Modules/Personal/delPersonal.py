from tabulate import tabulate
import os
import re
import json
import requests

#Servidor de Personal
def getAllDataPersonal():
	peticion = requests.get("http://154.38.171.54:5502/personas")
	data= peticion.json()
	return data

def ANumeroDePersonal(id):
    PersonalEncontrados = []
    for val in getAllDataPersonal():
        if val.get('nroId (CC, Nit)') == id:
            PersonalEncontrados.append(val)
            return PersonalEncontrados
    print('\nEl personal no existe')
    return PersonalEncontrados

#Servidor de Activos
def getAllDataActivos():
	peticion = requests.get("http://154.38.171.54:5502/activos")
	data = peticion.json()
	return data

def ActivosNumeroDeItem(NroItem):
    ItemEncontrados = []
    for val in getAllDataActivos():
        if val.get('NroItem') == NroItem:
            ItemEncontrados.append(val)
            return ItemEncontrados
    print('\nEl activo no existe')
    return ItemEncontrados


# NO SE PUEDE ELIMINAR PERSONAS QUE CUENTEN CON ACTIVOS ASIGNADOS.
#Deseamos eliminar un personal ya existente de la base de datos.
def deletePersonal(id):
    data =  ANumeroDePersonal(id), ActivosNumeroDeItem()
    if len(data):
            while True:
                os.system("cls") or ("clear")
                try:
                    if len(data[0]['asignaciones']) == 0:
                        data[0]['idEstado'] = "0"
                    else:
                        raise Exception("El personal que está intentando eliminar está asignado, por lo tanto no se puede eliminar.")                        
                except Exception as error:
                    print(error)
                break
            peticion = requests.put(f"http://154.38.171.54:5502/personas", data=json.dumps(data[0]).encode("UTF-8"))
            res = peticion.json()
            if 'Mensaje' in res:
                print(res['Mensaje'])
            input("Presione 0 (Cero) para volver: ")
            return [res]
    
  