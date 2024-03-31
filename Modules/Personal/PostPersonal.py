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

#Deseamos agregar a un personal nuevo a la base de datos.