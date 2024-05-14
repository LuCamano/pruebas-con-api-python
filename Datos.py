import json
import os

class Datos:
    def __init__(self) -> None:
        self.partes_disponibles = self.getPartesDisponibles()

    def getPartesDisponibles(self):
        data = []
        try:
            for filename in os.listdir("json"):
                if filename.endswith(".json"):
                    data.append(filename.split(".")[0])
            return data
        except:
            return None
    
    def getPartsByName(self, name):
        try:
            with open(f"json/{name}.json") as f:
                data = json.load(f)
            return data
        except:
            return None