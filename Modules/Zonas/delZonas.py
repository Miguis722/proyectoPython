from tabulate import tabulate
import os
import re
import json
import requests


#Servidor de Zonas
def getAllDataZonas():
	peticion = requests.get("http://154.38.171.54:5502/zonas")
	data= peticion.json()
	return data

