from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

# Import your functions from functions.py
from functions import  find_top_pop_venue_ratios, find_least_represented_restaurant_types_by_city

app = FastAPI()

# Index
@app.get("/", response_class=HTMLResponse)
async def index():
    template = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>NEXUSANALYTICS</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    padding: 20px;
                }
                h1 {
                    color: #333;
                    text-align: center;
                }
                p {
                    color: #666;
                    text-align: center;
                    font-size: 18px;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <h1>NexusAnalytics Recomendation Systems</h1>
            <p>Esta herramienta puede ser utilizada por inversores gastronómicos para encontrar las mejores oportunidades donde expandir sus franquicias o proponer nuevas.<p>
        </body>
    </html>
    """
    return HTMLResponse(content=template)


# ML endpoints:

@app.get("/Recomendación_de_ciudades/{top_n}")
async def read_Recomendación_de_ciudades(top_n : int):
    try:
        result = find_top_pop_venue_ratios(top_n)
        return result
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@app.get("/Recomendación_de_categorias/{city_name}/{top_n}")
async def read_Recomendación_de_categorias(city_name:str, top_n:int):
    try:
        result = find_least_represented_restaurant_types_by_city(city_name, top_n)
        return result
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))
