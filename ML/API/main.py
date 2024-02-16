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
                ul {
                    list-style-type: none;
                    padding: 0;
                }

                li {
                    width: 35%;
                    text-align: center;
                    margin-bottom: 20px;
                    font-family: Arial, sans-serif;
                    font-weight: bold;
                }

                .my-form {
                    display: flex;
                    align-items: left;
                    justify-content: left;
                }

                .my-form label {
                    margin-bottom: 7px;
                }

                .my-form .form-inputs {
                    margin-left: auto;
                }

                .my-form input[type="text"],
                .my-form input[type="number"],
                .my-form input[type="submit"] {
                    margin-left: auto;
                }

            </style>
        </head>
        <body>
            <h1>NexusAnalytics Recomendation Systems</h1>
            <p>Esta herramienta puede ser utilizada por inversores gastronómicos para encontrar las mejores oportunidades donde expandir sus franquicias o proponer nuevas.<p>
            <ul>
                <li>
                    <form action="/Recomendación_de_ciudades" method="get" class="my-form">
                        <label for="top_n">Recomendación_de_ciudades:</label>
                        <input type="number" id="top_n" name="top_n" required placeholder="N de Recomendaciones">
                        <input type="submit" value="Submit">
                    </form>
                </li>
                <li>
                    <form action="/Recomendación_de_categorias" method="get" class="my-form">
                        <label for="city_name">Ciudad de Florida:</label>
                        <input type="text" id="city_name" name="city_name" required placeholder="Ciudad de Florida">
                        <label for="top_n">N de Recomendaciones:</label>
                        <input type="number" id="top_n" name="top_n" required placeholder="N de Recomendaciones">
                        <input type="submit" value="Submit">
                    </form>

                </li>
            </ul>
        </body>
    </html>
    """
    return HTMLResponse(content=template)


# ML Endpoints:

@app.get("/Recomendación_de_ciudades")
async def read_Recomendación_de_ciudades(top_n : int):
    try:
        result = find_top_pop_venue_ratios(top_n)
        return result
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@app.get("/Recomendación_de_categorias")
async def read_Recomendación_de_categorias(city_name:str, top_n:int):
    try:
        result = find_least_represented_restaurant_types_by_city(city_name, top_n)
        return result
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
