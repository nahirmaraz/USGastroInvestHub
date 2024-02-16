![Nexus Portada](/Imagenes/Portada.jpg)
## ¡Bienvenidos a NexusAnalytics!
Somos una firma consultora que integra a ingenieros, científicos y analistas de datos para ofrecer soluciones personalizadas a nuestros clientes. Con un equipo multidisciplinario altamente calificado, combinamos conocimientos técnicos, creatividad y análisis profundo para brindar soluciones eficientes, permitiéndonos abordar una amplia gama de proyectos con excelencia. En NexusAnalytics, transformamos datos en información valiosa para impulsar el éxito empresarial.
## Introducción
La expansión de franquicias de restaurantes de comida étnica en ciudades del Sunbelt no solo representa un fenómeno de crecimiento económico, sino que también ofrece oportunidades significativas para inversores con diversos perfiles. Especialmente en lugares como Florida, la diversidad cultural, el atractivo turístico, la creciente población y la presencia de una comunidad latina vibrante convergen para potenciar el éxito de estas franquicias en un mercado en constante evolución.
![Comida](/Imagenes/Comida.JPG)

InnovaGastron Investments, una empresa inversora con raíces en América Latina, reconoce el potencial estratégico de esta expansión y se propone establecer su presencia en los Estados Unidos. Con una especialización en el sector de restaurantes en su país de origen, no solo busca oportunidades de inversión en la industria gastronómica estadounidense, sino que también tiene el objetivo de facilitar visas y traslados familiares para su equipo directivo.

Encomendándonos la tarea de analizar este emocionante escenario, InnovaGastron Investments busca nuestra experiencia para recopilar información clave sobre el tipo de restaurante más propicio para la inversión y determinar en qué ciudad de Florida, Estados Unidos se podrían maximizar los beneficios. Nuestra misión es proporcionar análisis estratégicos que permitan al inversor tomar decisiones informadas y exitosas en este proceso de expansión internacional.
## Alcance
El estudio de esta problemática se centra en la zona sur de Estados Unidos (Sunbelt) considerando los años mas recientes, es decir  2021-2023. Y se basa en el análisis de tres aspectos clave: 

1. Redes Sociales:
        Analizar la presencia en redes sociales, popularidad y percepción pública a través de plataformas masivas para entender las tendencias y expectativas locales.
2. Tráfico y Accesibilidad:
        Evaluar la accesibilidad y afluencia de clientes mediante el análisis de datos de tráfico en cada ubicación potencial.
3. Competencia y Restaurantes Establecidos:
        Investigar la competencia y restaurantes ya establecidos en las zonas consideradas, examinando reseñas, puntuaciones, tipos de restaurantes y otros factores relevantes.

Este alcance no incluirá decisiones financieras específicas como la asignación de presupuestos o detalles de inversión, pudiendo quedar para un futuro análisis; ni la gestión de visas y traslados familiares, que se considerarán tareas independientes.
## Objetivos
El objetivo de nuestro equipo es poder recomendar la mejor ubicación para la inversión del nuevo restaurante étnico de InnovaGastron Investments en Estados Unidos. Para lograrlo se realizaran las siguientes tareas, en base al alcance propuesto:
1. Analizar la Presencia en Redes Sociales:
* Realizar webscraping en Twitter para identificar la presencia y percepción pública de restaurantes de comida étnica en la zona sur de Estados Unidos.
* Cuantificar y analizar la actividad en redes sociales, centrándose en la popularidad y las tendencias locales para comprender la recepción del público.
2. Evaluar Accesibilidad y Afluencia de Clientes:
* Utilizar un dataset de estaciones de servicio para crear un mapa que visualice la ubicación de las estaciones en la zona sur de Estados Unidos.
* Relacionar la concentración de estaciones de servicio con la accesibilidad, identificando áreas con mayor afluencia de clientes potenciales para restaurantes de comida étnica.
3. Investigar Competencia y Restaurantes Establecidos:
 * Analizar datos de Google Maps y Yelp para obtener información detallada sobre la competencia y los restaurantes ya establecidos en la zona sur de Estados Unidos.
 * Aplicar análisis de sentimiento a reseñas y puntuaciones recopiladas, proporcionando una comprensión más profunda de la percepción del cliente y las fortalezas/deficiencias de los establecimientos existentes.
### Entregables
`Dashboard Interactivo:`
        Crear un dashboard interactivo en PowerBI que presente de manera visual y comprensible los resultados clave del análisis. Este dashboard incluirá gráficos, mapas, métricas relevantes y KPIs específicos, proporcionando a InnovaGastron Investments una visión integral de las oportunidades de inversión en restaurantes de comida étnica en la zona sur de Estados Unidos.

`API de Recomendación de ML:`
        Desarrollar una API en Render que disponibilice un sistema de recomendación basado en aprendizaje automático (ML). Esta API permitirá a InnovaGastron Investments acceder a recomendaciones personalizadas para la inversión en restaurantes, considerando preferencias de usuario, datos de accesibilidad y afluencia, así como información de competencia y establecimientos ya existentes.
        
[Nexus Recomendatios API](https://nexus-recomendations.onrender.com)
### Indicadores Clave de Rendimiento - KPIs
`KPI 1:` Índice de Popularidad en Redes Sociales (IPS)
* Métrica: Número total de menciones y interacciones en Twitter relacionadas con restaurantes de comida étnica en la zona sur de Estados Unidos.
* Fórmula: $\left( \frac{{N° Total De Menciones + N° De Interacciones}}{{Total De Restaurantes Analizados}} \right) \times 100$

`KPI 2:` Tendencia de Hashtags Locales
* Métrica: Frecuencia y popularidad de hashtags locales relacionados con comida étnica.
* Fórmula: No aplicable directamente. Se mide la variación de hashtag a travéz del tiempo por medio de un gráfico.

`KPI 3:`Índice de Satisfacción del Cliente (ISC)
* Métrica: Puntuaciones y reseñas de Google Maps y Yelp.
* Fórmula: $\left( \frac{{Puntuación Promedio*N° De Reseñas}}{{Total De Reastaurantes Analizados}} \right) \times 100$

`KPI 4:`Proporción de Reseñas Positivas y Negativas
* Métrica: Análisis de sentimiento para clasificar las reseñas como positivas o negativas.
* Fórmula: $\left( \frac{{N° Reseñas Positivas}}{{Total De Reseñas Realizadas}} \right) \times 100$


## Metodología de trabajo
![Diagrama Scrum](/Imagenes/SCRUM.jpg)
- Roles

    `Product owner:`El product owner (PO) representa a los stakeholders (interesados externos o internos) y tiene la responsabilidad de asegurar que el equipo trabaje eficientemente. Proporciona claridad y dirección.

    `Scrum master:`El scrum master se encarga de asegurar que el equipo siga sus reglas y prácticas. Su rol es crucial tanto para la implementación de los eventos de Scrum, como para mantener un flujo de comunicación abierto y efectivo entre el equipo y el PO. Ayuda a eliminar cualquier obstáculo que el equipo pueda encontrar durante el desarrollo del proyecto, lo que permite que el proceso fluya sin problemas. 

    `Team:`El team, o equipo de desarrollo, está compuesto por los profesionales que realizan el trabajo de crear y entregar el producto mejorado en cada sprint. 

- Eventos 

    `Sprint Backlog:` El backlog del sprint es una lista de elementos  seleccionados (hitos) que el equipo se compromete a completar en un sprint específico. Es una herramienta crucial para planificar y organizar el trabajo en cada sprint, y se gestiona por el equipo de desarrollo con la guía del scrum master y el product owner.

    `Planning:`Todos los miembros del equipo encargados de llevar a cabo el sprint se reúnen y deciden los requerimientos del mismo, diseñan la división de tareas y asignan a cada una un periodo de tiempo. Se trata de una manera de planificar más horizontal. Esto se logra gracias al panel de tareas, una herramienta visual que muestra las tareas que se asignan a cada miembro del proyecto y el estado de cada tarea (por ejemplo, pendiente, en progreso o completada). Este panel ayuda a los miembros del equipo a tener una visión clara del progreso del sprint y a identificar cuellos de botella o áreas que requieren atención adicional. También fomenta la transparencia y la comunicación dentro del equipo, al proporcionar una vista clara del trabajo en curso y quién es responsable de cada tarea.

    `Implementation:` El equipo pone en marcha la planificación del Sprint, respetando los roles y tiempos. Para eso cuenta con la ayuda del Scrum Master con quien realiza reuniones diarias (de unos 15 minutos de duración) que deben mantenerse siempre a la misma hora y en el mismo sitio, para crear un mindset adecuado en el equipo.  Su objetivo es responder a tres preguntas clave: qué se hizo el día anterior, cuál es el plan del día y qué obstáculos aparecieron durante el proceso. Si surge algún tema que necesita de más tiempo para resolverse, no se hará en el team meeting, sino que se convocará una reunión específica. La idea principal es aprovechar el tiempo al máximo.

    `Review:`Se trata de reuniones semanales entre el Team, el Scrum Master y el Product Owner,en el que se muestra el avance del proyecto. Aunque todos los miembros del equipo están presentes, la reunión la lideran el Project Owner y el Scrum Master. El objetivo es comprender qué se hizo bien y averiguar si existe espacio de mejora. También se analizan los inconvenientes que el equipo encontró y el manejo del tiempo.

    `Retrospect:`Se trata de una reunión post-sprint entre los miembros del equipo y el Scrum Master para discutir lo que salió bien, lo que no, y cómo mejorar. Luego de esta reunión puede ser necesaria la reestructuración de la planificación del Sprint.

    `Definition of done:` Producto final del Sprint listo para la entrega al cliente.
- Beneficios de Scrum

   * Adaptabilidad y flexibilidad: permite adaptarse a los cambios en los requisitos del proyecto con relativa facilidad, lo cual es crucial en entornos dinámicos.
   * Entrega continua: los equipos pueden entregar resultados de manera continua a través de los Sprints, que son ciclos de desarrollo cortos y time-boxed.
   * Colaboración y comunicación mejoradas: fomenta la colaboración entre los miembros del equipo y el cliente, permitiendo una toma de decisiones más rápida.
   * Retroalimentación temprana y frecuente: los clientes pueden ver y revisar el progreso del proyecto en etapas tempranas, lo que permite incorporar su feedback con rapidez. 
   * Visibilidad del progreso: las reuniones diarias y las revisiones al final de cada Sprint proporcionan una visibilidad clara del estado del proyecto a todas las partes interesadas.
  *  Optimización del tiempo y los recursos: Scrum ayuda a optimizar la utilización de los recursos y el tiempo, asegurando que el trabajo se realice de la manera más eficiente posible.
   * Innovación: al trabajar en ciclos cortos y recibir feedback constante, los equipos tienen la oportunidad de innovar y mejorar el producto de forma continua.
   * Reducción de riesgos: scrum permite identificar y abordar los riesgos en las primeras etapas del proyecto, lo cual ayuda a prevenir males mayores en el futuro.
## Desarrollo
A continuación se muestran los diagramas de Gantt hechos para el desarrollo de las tareas, asi también como los roles y responsables del mismo, divididos por sprints.
* Sprint 1
![Hitos del primer Sprint](/Imagenes/Sprint1.png)
* Srint 2
![Hitos del segundo Sprint](/Imagenes/Sprint2.png)
* Sprint 3
![Hitos del tercer Sprint](/Imagenes/Sprint3.png)
### Pipeline General
![Pipeline General](/Imagenes/StackPipeline.jpg)

### Pipeline ETL
![Pipeline ETL](/Imagenes/PipelineProcesoETL.jpg)
### Diagrama Entidad-Relación
![Pipeline ETL](/Imagenes/DiagramaER.jpg)
## Estructura del proyecto:
-[Estructura](https://github.com/pono33/USGastroInvestHub/tree/main/Desarollo%20del%20Proyecto): en el siguiente link se muestran, separados por Sprints, el paso a paso de las tareas realizadas para este proyecto.
## Resultados:
![Scursales_YELP](/Imagenes/TipoSucursales_YELP.png)
En este gráfico se puede ver que, en base a la plataforma YELP, la comida mexicana está dentro del top 3 de comidas étnicas, siguiéndole la intaliana y la china.
![Sucursales_GM](/Imagenes/TipoSucursales_GM.png)
En el siguiente gráfico se observa el ranquing segun Google Mpas. Hay un cambio de posiciones, sin embargo el top 3 se mantiene igual.
![Frecuencia_Franquicia_YELP](/Imagenes/FrecuenciaFranquicias_YELP.png)
En la imagen se observa la frecuencia de las franquicias segun YELP. Siendo 'Taco Bell' la mas numerosa, que junto a 'Chiplote Mexican Grill' y 'QDOBA Mexican Eats' cinforman la etnia mas popular.
![Frecuencia_Franquicias_GM](/Imagenes/FrecuenciaFranquicias_GM.png)
En la imagen se observa que también predomina 'Taco Bell en la plataforma de Google Maps, sin embargo ahora la acompaña solo 'Chiplote Mexican Grill'. En cambio a la comida china (la mas popular) la acompañan 'China Wok', 'China KING' 'China Max' y 'China Star'.
![CheckIn_YELP](/Imagenes/CheckIn_YELP.png)
En la siguiente imagen se observa como varia la cantidad de reservas segun el mes del año, segun la plataforma YELP. Siendo Julio su maximo punto de Chech in, bajando drasticamente hasta Septiembre y recuperándose de nuevo en Octubre.
![ClientesPotenciales_YELP](/Imagenes/ClientesPotenciales_YELP.png)
El siguiente gráfico se muestra la variación de personas que hacen reviews en el transcurso del año segun YELP. Estos son clientes potenciales por haber concurrido al establecimiento al menos una vez. Existe una correlación con la cantidad de reservas, ya que los meses con mayor numero de clientes potenciales son Junio, Julio y Agosto, bajando en Septienmre.
![ClientesPotenciales_GM](/Imagenes/ClientesPotenciales_GM.png)
En la imagen se ve la variación de clientes potenciales segun Google Mpas. Los mejores meses son los de Abril a Mayo, bajando drásticamente hacia Septiembre.
![SentimentAnalysis_YELP](/Imagenes/SentimentAnalysis_YELP.png) El gráfico muestra la proporcion de reseñas negativas (90%), neutrales (%7), positivas (%2) y muy positivas (%0,5) según la plataforma de YELP.
![SentimentAnalysis_GM](/Imagenes/SentimentAnalysis_GM.png) El gráfico muestra la proporcion de reseñas negativas (80%), neutrales (%8), positivas (%9) y muy positivas (%3) según la plataforma de Google Maps.
![FrecuenciaHastags](/Imagenes/FrecuenciaHashtagsLocales.png)
En el siguiente gráfico se ve la variación del uso de los hashtags mas populares en Twitter a cerca de comida etnica en USA. Siendo genericamente los mas utilizados, 'food' y 'restaurant', siguiéndoles 'chinese', 'italian' y 'mexican'.

## Conclusiones:
Considerando que la comida china se encuentra en el puesto número uno segun dos de nuestras fuentes, Twitter y Google Mpas, recomendamos la inversion en ese tipo de ethnia, siendo la mejor franquicia 'China WOK' por la satisfacción del cliente. También se recomienda que el lugar geográfico sea por la zona costera de Miami Beach o Tampa, debido que en esos lugares se visualiza mayor flujo de tráfico y accesibilidad.

## Autores
![Autores](/Imagenes/caras.jpg)

|  [Alvaro Alvarez Cardenas](https://www.linkedin.com/in/alvaro-javier-alvarez-cardenas-81696056/) - | - [Gabriel Chumbes](https://www.linkedin.com/in/gabriel-chumbes-rueda-b30967a2/) - | - [Erwin Alain Tayro](https://www.linkedin.com/in/alain-tayro/) - | - [Facundo Graziola](https://www.linkedin.com/in/facundo-graziola/) - | - [Marlen Nahir Maraz](https://www.linkedin.com/in/marlen-nahir-maraz-581657168/)  | 
|--|--|--|--|--|



