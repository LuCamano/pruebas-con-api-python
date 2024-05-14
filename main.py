from fastapi import FastAPI, HTTPException
import Datos

app = FastAPI()
datos = Datos.Datos()

@app.get("/")
async def root():
    return datos.partes_disponibles



@app.get("/total/{partName}/")
async def getPart(partName: str):
    if datos.getPartsByName(partName) == None:
        raise HTTPException(status_code=404, detail="Parte no encontrada")
    return len(datos.getPartsByName(partName))



@app.get("/{partName}/")
async def getPart(partName: str):
    if datos.getPartsByName(partName) == None:
        raise HTTPException(status_code=404, detail="Parte no encontrada")
    return datos.getPartsByName(partName)



@app.get("/{partName}/{id}/")
async def getPart(partName: str, id: int):
    if datos.getPartsByName(partName) == None:
        raise HTTPException(status_code=404, detail="Parte no encontrada")
    return datos.getPartsByName(partName)[id-1]



@app.get("/{partName}/{id}/{parameter}/")
async def getPart(partName: str, id: int, parameter: str):
    if datos.getPartsByName(partName) == None:
        raise HTTPException(status_code=404, detail="Parte no encontrada")
    return datos.getPartsByName(partName)[id-1][parameter]