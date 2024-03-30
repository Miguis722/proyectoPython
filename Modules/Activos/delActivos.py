from tabulate import tabulate
import os
import re
import json
import requests

#Servidor de Activos
def getAllDataActivos():
	peticion = requests.get("http://154.38.171.54:5502/activos")
	data = peticion.json()
	return data

#Deseamos eliminar un activo por medio de su id o su 