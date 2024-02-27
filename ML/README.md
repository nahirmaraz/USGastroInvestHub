# Modelo de Machine Learning

Teniendo los metadatos de los restaurantes se recurre a una fuente adicional de información: ‘census.gov’, con esta información adicional seremos capaces de tener información sobre las coordenadas estándares de las ciudades así también como de aquellos lugares más poblados para tenerlos a consideración. Con esto seremos capaces de filtrar aún más la data. Posteriormente a esto se busca clusterizar aquellas ciudades con distribución similar en restaurantes, luego calculamos la desviación estándar entre estos clústeres para que al final podamos encontrar con toda esta información aquellos restaurantes menos representados por ciudad.

Estas categorías se han elegido con el fin de considerar grupos más representativos y evitar la dispersión de información al entrenar el modelo de recomendación.

## Categorías Principales:
- Latin
- Asian
- European
- Others
- American
- Italian
- Chinese
- Mexican
- Cafe
- Beverages
- Others

## Subcategorías:

- **European:** Greek, French, German, Spanish, Catalan, Basque,Galician, Sicilian, English, Scottish, Welsh, Irish, Dutch, Swedish, Polish, Portuguese, Irish Pub.
- **Italian:** Pasta.
- **Latin:** Empanadas, Lomo, Asado, Locro, Dulce de Leche, Choripan, Argentinian, Peruvian, Ceviche, Pisco, Mexican, Tacos, Burritos, Enchiladas, Colombian, Arepas, Brazilian.
- **Asian:** Sushi, Ramen, Pan-Asian, Korean, Kimchi, Japanese, Sashimi, Tempura, Thai, Vietnamese, Indian.
- **American:** Steak, Fast Food, Hamburger, Fast, Chicken wings, Cheesesteak, Sandwich, Fried chicken, Buffet, Restaurant, Brasserie.
- **Cafe:** Tea, Dinner, Cafe, Coffee.
- **Beverages:** Beer, Caterer, Cocktail, Pub, Brewpub.
- **Others:** Healthy, Vegetarian, Vegan, Casual, Seafood, Bistro, African, Middle Eastern, Hummus, Falafel, Shawarma, Tabbouleh, Israeli, Shakshuka, Lebanese, Iranian, Jewish, Turkish.
  
## Justificación:
La clasificación de los restaurantes en estas categorías principales y subcategorías proporciona una estructura organizativa que facilita la gestión y el análisis de la información. Esto será beneficioso tanto para los propietarios de restaurantes que deseen comprender mejor su mercado objetivo como para los desarrolladores que trabajan en sistemas de recomendación y análisis de datos relacionados con la industria gastronómica.




