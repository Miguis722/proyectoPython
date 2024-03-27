import json
import requests

#Servidor de Categorias
def getAllDataCategorias():
    peticion = requests.get("http://154.38.171.54:5502/categoriaActivos")
    data = peticion.json()
    return data

#codigo1 = "Equipo de Computo"
#codigo2 = "Electrodomestico"
#codigo3 = "Juego"