import pandas as pd

# Datasets import
from data import cities_FL, std_dfs

# API Functions:    

def find_top_pop_venue_ratios(top_n : int):
    '''
    Esta función ayuda a los usuarios a encontrar las mejores ciudades en las cuales desarrollar emprendimientos gastronómicos o extender cadenas gastronómicas.

    Args:
        top_n: Número de recomendaciones que se desean obtener (int).

    Returns: 
        El diccionario generado describiendo el número de ciudades solicitadas.
    '''
    
    # Ordenar el DataFrame por la relación de población/venue en orden descendente
    sorted_df = cities_FL.sort_values(by='pop_venue_ratio', ascending=False)
    
    # Seleccionar las primeras top_n filas
    top_pop_venue_ratio_df = sorted_df.head(top_n)[['cluster', 'city', 'pop_venue_ratio']]
    
    # Restablecer el índice del DataFrame resultante
    top_pop_venue_ratio_df.reset_index(drop=True, inplace=True)
    
    # Construir y devolver diccionario
    return [{'{}'.format(i + 1): city} for i, city in enumerate(top_pop_venue_ratio_df)]


def find_least_represented_restaurant_types_by_city(city_name:str, top_n:int):
    '''
    Esta función ayuda a los usuarios a encontrar las categorias gastronómicas con menor competencia, como mejores opciones a desarollar.

    Args:
        city_name: Nombre de la ciudad (En Florida) sobre la cual se desea consultar.
        top_n: Número de recomendaciones que se desean obtener (int).

    Returns: 
        El diccionario generado describiendo el número de categorias solicitadas.
    '''
    # Buscar la fila correspondiente a la ciudad en cities_FL
    city_row = cities_FL[cities_FL['city'] == city_name]

    if city_row.empty:
        print(f"No se encontró información para la ciudad {city_name}.")
        return None

    # Obtener el clúster de la ciudad
    cluster = city_row['cluster'].iloc[0]

    # Seleccionar el DataFrame correspondiente al clúster de la ciudad
    city_std_df = std_dfs[cluster]

    # Encontrar los tipos de restaurantes menos representados en la ciudad
    least_represented = city_std_df.nsmallest(top_n, city_name, keep='all')[city_name]

    # Crear un DataFrame con los resultados
    least_represented_df = pd.DataFrame({'Restaurant Type': least_represented.index,
                                         'Frequency Difference': least_represented.values})

    # Agregar una columna con el número de tipo de restaurante (índice)
    least_represented_df['Rank'] = range(1, top_n + 1)

    # Establecer el nombre de la ciudad como índice del DataFrame
    least_represented_df.set_index('Restaurant Type', inplace=True)

    # Construir y devolver diccionario
    return [{'{}'.format(i + 1): category} for i, category in enumerate(least_represented_df['Restaurant Type'])]

