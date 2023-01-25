import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import dash_table
from dash.exceptions import PreventUpdate
import pandas as pd
import plotly.graph_objs as go
import os
import unicodedata
import requests
import json
import wikipedia
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import sqlite3
from app import app
import dash_gif_component as gif


carrusel = [
    {"key": "1", "src": "/assets/im3_1_edited.png"},
    {"key": "2", "src": "/assets/im3_2_edited.png"},    
    {"key": "3", "src": "/assets/im3_3_edited.png"},    
    ]

tooltip = {
    1:"Planillas, documentos, BDs, otras fuentes",
    2:"Nuevos datos, relaciones, patrones y tendencias",
    3:"Modelos, proyecciones y predicciones",
    4:"Aplicación Web, APIs, Reportes, otros",
    5:"Mejoras y desarrollo de herramientas",
}    

etapasIA = {
    1:"A partir de los objetivos de la organización se inicia un proyecto de implementación de IA identificando el estado tecnológico de la empresa y la información disponible.",
    2:"Con los datos disponible investigamos patrones y relaciones que permitirán modelar el problema atacado y crear soluciones novedosas.",    
    3:"Empleando IA se aislan las soluciones más efectivas, optimizando su configuración hasta lograr los estándares fijados por la empresa.",
    4:"Generamos la infraestructura tecnológica necesaria para aplicar las soluciones creadas a las tareas cotidianas de la empresa. El foco está puesto en la robustez y usabilidad.",
    5:"Controlamos el desempeño de los modelos, verificando su conformidad a los objetivos de la empresa, buscando oportunidades de mejorar sus resultados.",
}

etapasdetailIA = {
    1: "Al inicio, luego de las definiciones de la empresa sobre objetivos y alcance del proyeto, se recolectan y preparan los datos para analizarlos. Se accede regularmente a diferentes fuentes, se procesa y combina la información almacenada para integrarla en un conjunto sistemático y coherente. Usualmente aquí empezamos a ver grandes volúmenes de información (Big Data). Luego se realiza una exploración de los datos para comprender su estado y características, anomalías, faltantes e inconsistencias.",
    2: "En esta segunda etapa se generan transformaciones en los datos para adaptarlos al problema que se busca resolver y 'potenciar' la porción de información que es más útil para eso. Se realizan tareas como normalización, escalado, codificación y generación de características. También se crean nuevos conjuntos de datos que codifican información relevante para las etapas siguientes.",
    3: "En esta tercera etapa se crean y 'entrenan' los modelos más apropiados para el problema empleando los datos preparados en las etapas anteriores. Se evalúan los resultados de los diferentes experimentos, y se itera sobre aquellos que presentan mayor proyección. Por último se diseña la solución definitiva para las necesidades de la empresa, asegurándonos que el modelo funciona correctamente ",
    4: "En esta cuarta etapa se implementa el modelo en un entorno de producción y se integra con otras aplicaciones o sistemas.",
    5: "Finalmente, en esta última etapa se monitorea el rendimiento del sistema y analizan oportunidades de mejorando. Frecuentemente, se incorporan nuevos datos, se revisan y reentrenan modelos.",
}

etapasdetailIA_header_graph = {
    "result1":"Resultados: vías de transferencia datos, información integrada y consolidada",
    "detail1":"Se crea un modelo de datos integrados y sistemático, permitiendo análisis multidimensionales de la organización con alcance a la información recolectada.",
    "result2":"Resultados: nuevos datos, patrones y proyecciones",
    "detail2":"Surge una nueva comprensión de la realidad organizacional y del entorno de la empresa que permite acciones inmediatas.",
    "result3":"Resultados: modelos inteligentes que atacan el problema abordado",
    "detail3":"La información que proveen los modelos no solo ofrece una respuesta a los problemas abordados por el proyecto, permiten además extender al resto de la organización (ej.Logística, Operaciones, Contabilidad, etc.) cambios y mejoras.",
    "result4":"Resultados: aplicaciones y herramientas basadas en los modelos creados",
    "detail4":"Se construyen los dispositivos de consulta y herramientas de trabajo que implementan la solución elaborada en la etapa anterior.",
    "result5":"Resultados: actualización y desarrollo de la solución",
    "detail5":"La experiencia en la implementación de la herramiento y los nuevos datos son reintroducidos periódicamente en la solución diseñada fortaleciendo su desempeño.",  
}



problemas = [
    dbc.CardHeader("Card header"),
    dbc.CardBody(
        [
            #html.H5("Card title", className="card-title"),
            html.P(
                dcc.Markdown('''
                Multiplo es un empresa dedicada a mejorar procesos                                                            
                '''
                ),       
            ),
        ]
    ),
]

creditos = [
    dbc.Col(
        html.P(
                dcc.Markdown('''
                Credits for animations: 
                [xponentialdesign](https://giphy.com/xponentialdesign),
                [Alastair Gray](https://giphy.com/alastairgray")                                                                  
                '''
                ),       
            ),
        style = {"font-size": 12,},
        width={"size": 2, "offset": 1},
    )  
]

pie = [
    dbc.Col(html.Div("Paraná, Entre Ríos Argentina."), width=2),
    dbc.Col(html.Div("multiplo@algunmail.com"), width=2),
]

def layout():
    return [
        html.Div(            
            [   
                # Carrusel, primera frase y Contacto----
                dbc.Row(                                       
                        children=[
                            dbc.Col(html.Div(
                                [
                                    dbc.Card(
                                         dbc.Carousel(
                                            items= carrusel,                                       
                                            class_name="carousel-fade",
                                            controls=True,
                                            indicators=True,
                                            interval=3000,
                                            variant="dark",                                            
                                            #ride="carousel",
                                            style={                                                
                                                "border-radius": "10px",                                                
                                                "background-color": "black", #white = "rgba(0,0,0,0)",
                                                "overflow": "hidden",                                                
                                            }
                                    ),
                                    style={
                                        "border": "none",
                                    }
                                    )
                                ]                                    
                            ),
                            width=6,                             
                            ),
                            dbc.Col(html.Div(
                                children=[
                                    dmc.Text(
                                        "Multiplo es un empresa dedicada a mejorar procesos empresariales aplicando Inteligencia Artificial o IA. De datos caóticos a nuevos productos, brindamos sistemas avanzados para mejorar los márgenes y la rentabilidad del negocio.",
                                        variant="gradient",
                                        gradient={"from": "skyblue", "to": "fuchsia", "deg": 100},
                                        style={"fontSize": 30},
                                    ),
                                    html.Br(),
                                    html.Br(),
                                    dmc.Text(
                                        "¿Dispones de datos? Multiplo se ocupa del sistema para generar conocimiento.",                                        
                                        color="white",
                                        style={"fontSize": 20},                                    
                                    ),
                                    html.Br(),
                                    html.Br(),
                                    html.Div(
                                        [
                                            dbc.Button("Conocer nuestras soluciones", outline=True, color="primary", className="me-md-2"),
                                            dbc.Button("Comunicarse con ventas", outline=True, color="info", className="me-md-2"),
                                        ],
                                        #className="d-grid gap-2 col-6 mx-auto lg-1",                        
                                    )
                                ]                                
                                #dcc.Markdown('''                                    
                                #    > Multiplo es un empresa dedicada a mejorar procesos
                                #    > aplicando Inteligencia Artificial **(IA)** en tareas humanas.                                                   
                                #    '''
                                #    ),                                
                                #style = {
                                #    "font-size": 30,
                                #},
                            ),
                            width=6,
                        )
                    ],
                    align = "center", 
                    ),                
                html.Br(),
                html.Br(),
                html.Br(),  
                html.Br(),  
                html.Br(),                   
                # ML Title ----
                html.Div(
                    [
                        dbc.Row(
                                [
                                    dbc.Col(html.Div(""),
                                    width=2,
                                    ),
                                    dbc.Col(html.Div(
                                        children=[
                                            dmc.Text(
                                                "Multiplo te acompaña a incoporar IA en tu empresa",
                                                variant="gradient",
                                                gradient={"from": "fuchsia", "to": "skyblue", "deg": 100},
                                                style={"fontSize": 30},
                                            ),
                                            html.Br(),
                                            dmc.Text(
                                                "en ese proyeto cada etapa es una unidad con resultados valiosos",                                        
                                                color="white",
                                                style={"fontSize": 20},
                                            ),
                                        ]),                                        
                                        style={
                                            'text-align': 'center',                                            
                                        }, 
                                        width=8,  
                                    ),
                                    dbc.Col(html.Div(""),
                                     width=2,
                                    ),
                                ],
                        )                      
                    ],                    
                ),
                html.Br(),  
                html.Br(), 
                html.Br(),                 
                # ML Pipeline Graph             
                dbc.Row(
                    [
                        dbc.Col(
                            dmc.Card(
                                children=[
                                    dmc.CardSection(
                                        dmc.Image(
                                            src= app.get_asset_url("document.png"),                                            
                                            radius="lg",
                                        ),
                                        id="liq1",
                                        ),  
                                        dbc.Tooltip(
                                                tooltip[1],
                                                target="liq1",
                                                placement = "top",
                                        ),
                                        html.Br(),                                  
                                        dmc.Group(
                                            [                                                
                                                dbc.Button("1. Acceso", 
                                                    outline=True, 
                                                    color="info",
                                                    size="md", 
                                                    href="#acceso", 
                                                    external_link=True,                                              
                                                    #disabled=True,
                                                ),                                                                                                                                   
                                                #dmc.Text("Acceso a Datos",
                                                #size="lg",
                                                #color="dimmed",
                                                #),
                                            ],
                                            position="center",
                                            mt="md",
                                            mb="xs",
                                        ),
                                    html.Br(), 
                                    dmc.Center(
                                        children=[
                                            dmc.Text(
                                                etapasIA[1],
                                                size="lg",
                                                color="dimmed",
                                            )
                                        ]
                                    ),                                        
                                    #dmc.Button(
                                    #    "Book classic tour now",
                                    #    variant="light",
                                    #    color="blue",
                                    #    fullWidth=True,
                                    #    mt="md",
                                    #    radius="md",
                                    #),
                                ],
                                #withBorder=True,
                                #shadow="sm",
                                radius="md",
                                #style={"width": 200},
                                className="border-1 bg-transparent",
                            )),
                        dbc.Col(
                            dmc.Card(
                                children=[
                                    dmc.CardSection(
                                           dmc.Image(
                                            src= app.get_asset_url("approval.png"),                                            
                                            radius="lg",
                                        ),
                                        id="liq2",
                                    ),
                                    dbc.Tooltip(
                                            tooltip[2],
                                            target="liq2",
                                            placement = "top",
                                    ),
                                    html.Br(),
                                    dmc.Group(
                                        [
                                            #dmc.Text("Norway Fjord Adventures", weight=500),
                                            #dmc.Badge("Integración", color="gray", variant="dark"),
                                            dbc.Button("2. Transformación", 
                                                outline=True, 
                                                color="info",
                                                size="md",
                                                href="#transformacion", 
                                                external_link=True,      
                                                #disabled=True,
                                            ),
                                        ],
                                        position="center",
                                        mt="md",
                                        mb="xs",
                                    ),
                                    html.Br(),
                                    dmc.Center(
                                        children=[
                                            dmc.Text(
                                                etapasIA[2],
                                                size="lg",
                                                color="dimmed",
                                            )
                                        ]
                                    ),      
                                    #dmc.Button(
                                    #    "Book classic tour now",
                                    #    variant="light",
                                    #    color="blue",
                                    #    fullWidth=True,
                                    #    mt="md",
                                    #    radius="md",
                                    #),
                                ],
                                #withBorder=True,
                                #shadow="sm",
                                radius="md",
                                #style={"width": 200},
                                className="border-1 bg-transparent",                                
                            )),
                        dbc.Col(
                            dmc.Card(
                                children=[
                                    dmc.CardSection(
                                           dmc.Image(
                                            src= app.get_asset_url("dashboard.png"),                                            
                                            radius="lg",
                                        ),
                                        id="liq3",
                                    ),
                                    dbc.Tooltip(
                                            tooltip[3],
                                            target="liq3",
                                            placement = "top",
                                    ),
                                    html.Br(),
                                    dmc.Group(
                                        [
                                            #dmc.Text("Norway Fjord Adventures", weight=500),
                                            #dmc.Badge("Integración", color="gray", variant="dark"),
                                            dbc.Button("3. Generación", 
                                                outline=True, 
                                                color="info",
                                                size="md",
                                                href="#generacion", 
                                                external_link=True,      
                                                #disabled=True,
                                            ),
                                        ],
                                        position="center",
                                        mt="md",
                                        mb="xs",
                                    ),
                                    html.Br(),
                                    dmc.Center(
                                        children=[
                                            dmc.Text(
                                                etapasIA[3],
                                                size="lg",
                                                color="dimmed",
                                            )
                                        ]
                                    ),      
                                    #dmc.Button(
                                    #    "Book classic tour now",
                                    #    variant="light",
                                    #    color="blue",
                                    #    fullWidth=True,
                                    #    mt="md",
                                    #    radius="md",
                                    #),
                                ],
                                #withBorder=True,
                                #shadow="sm",
                                radius="md",
                                #style={"width": 200},
                                className="border-1 bg-transparent",
                            )),
                        dbc.Col(
                            dmc.Card(
                                children=[
                                    dmc.CardSection(
                                           dmc.Image(
                                            src= app.get_asset_url("share.png"),                                            
                                            radius="lg",
                                            ),
                                            id="liq4",
                                        ),
                                        dbc.Tooltip(
                                                tooltip[4],
                                                target="liq4",
                                                placement = "top",
                                        ),
                                    html.Br(),
                                    dmc.Group(
                                        [
                                            #dmc.Text("Norway Fjord Adventures", weight=500),
                                            #dmc.Badge("Integración", color="gray", variant="dark"),
                                            dbc.Button("4. Producción", 
                                                outline=True,                                                 
                                                color="info",
                                                size="md",
                                                href="#produccion", 
                                                external_link=True,      
                                                #disabled=True,
                                            ),
                                        ],
                                        position="center",
                                        mt="md",
                                        mb="xs",
                                    ),
                                    html.Br(),                                    
                                    dmc.Center(
                                        children=[
                                            dmc.Text(
                                                etapasIA[4],
                                                size="lg",
                                                color="dimmed",
                                            )
                                        ]
                                    ),      
                                    #dmc.Button(
                                    #    "Book classic tour now",
                                    #    variant="light",
                                    #    color="blue",
                                    #    fullWidth=True,
                                    #    mt="md",
                                    #    radius="md",
                                    #),
                                ],
                                #withBorder=True,
                                #shadow="sm",
                                radius="md",
                                #style={"width": 200},
                                className="border-1 bg-transparent",
                            )),
                        dbc.Col(
                                dmc.Card(
                                    children=[
                                        dmc.CardSection(
                                             dmc.Image(
                                                src= app.get_asset_url("setting.png"),                                            
                                                radius="lg",
                                            ),
                                            id="liq5",
                                        ),
                                        dbc.Tooltip(
                                                tooltip[5],
                                                target="liq5",
                                                placement = "top",
                                        ),
                                        html.Br(),
                                        dmc.Group(
                                            [                                                
                                                dbc.Button("5. Mejora", 
                                                    outline=True, 
                                                    color="info",
                                                    size="md", 
                                                    href="#produccion", 
                                                    external_link=True,   
                                                    #disabled=True,
                                                ),
                                            ],
                                            position="center",
                                            mt="md",
                                            mb="xs",
                                        ),
                                        html.Br(),
                                        dmc.Center(
                                            children=[
                                                dmc.Text(
                                                    etapasIA[5],
                                                    size="lg",
                                                    color="dimmed",
                                                )
                                            ]
                                        ),      
                                        #dmc.Button(
                                        #    "Book classic tour now",
                                        #    variant="light",
                                        #    color="blue",
                                        #    fullWidth=True,
                                        #    mt="md",
                                        #    radius="md",
                                        #),
                                    ],
                                    #withBorder=True,                                
                                    #shadow="sm",
                                    radius="md",
                                    #style={"width": 200},
                                    className="border-1 bg-transparent",                                
                                )),
                    ]
                ),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                # ML Pipelina Detail ----
                dbc.Row(
                    html.Div(
                        [                                 
                            dbc.Row(
                                children=[                                    
                                    dbc.Col(
                                        html.Div(
                                            children=[
                                                html.Div(
                                                     dmc.Badge(
                                                        "1. Acceso",
                                                        variant="gradient",
                                                        gradient={"from": "grape", "to": "pink", "deg": 35},
                                                        id="acceso", 
                                                        size="xl",
                                                    ),                                                   
                                                ),                                                 
                                                html.Br(),
                                                dmc.Text(
                                                    etapasdetailIA[1],                                                
                                                    variant="gradient",
                                                    gradient={"from": "skyblue", "to": "fuchsia", "deg": 100},
                                                    style={"fontSize": 20},
                                                ),                                                 
                                            ],                                                                                    
                                        ),
                                        width=4,
                                        align = "top",
                                        style={'text-align': 'right'},
                                    ),
                                    dbc.Col(
                                        dmc.Card(
                                                children=[
                                                     dmc.CardSection(
                                                        dmc.Group(
                                                            children=[
                                                                dmc.Text(etapasdetailIA_header_graph["result1"], 
                                                                    weight=500,
                                                                    variant="gradient",
                                                                    gradient={"from": "blue", "to": "fuchsia", "deg": 100},
                                                                    style={"fontSize": 20},
                                                                ),                                                                
                                                            ],
                                                            position="apart",
                                                        ),
                                                        withBorder=True,
                                                        inheritPadding=True,
                                                        py="xs",
                                                    ),
                                                    dmc.Text(
                                                        children=[
                                                            dmc.Text(
                                                                etapasdetailIA_header_graph["detail1"],
                                                            )
                                                        ],
                                                        mt="sm",
                                                        color="dimmed",
                                                        size="sm",
                                                    ),
                                                    dmc.CardSection(
                                                        dmc.Image(
                                                            src=app.get_asset_url("csv_file.png"),
                                                            mt="sm",
                                                        ),
                                                    ),
                                                    
                                                ],
                                                withBorder=True,
                                                shadow="sm",
                                                radius="lg",                                                
                                            ),
                                        width={"size": 6, "offset": 1},                                        
                                    ),
                                ]
                            ),    
                            html.Br(),
                            html.Br(),
                            html.Br(), 
                            dbc.Row(
                                children=[ 
                                    dbc.Col(
                                        html.Div(
                                            children=[
                                                html.Div(
                                                     dmc.Badge(
                                                        "2. Transformación",
                                                        variant="gradient",
                                                        gradient={"from": "grape", "to": "pink", "deg": 35},
                                                        id="transformacion", 
                                                        size="xl",
                                                    ),                                                   
                                                ),                                                 
                                                html.Br(),
                                                dmc.Text(
                                                    etapasdetailIA[2],                                                
                                                    variant="gradient",
                                                    gradient={"from": "skyblue", "to": "fuchsia", "deg": 100},
                                                    style={"fontSize": 20},
                                                ),                                                 
                                            ],                                                                                    
                                        ),
                                        width=4,
                                        align = "top",
                                        style={'text-align': 'right'},
                                    ),
                                    dbc.Col(
                                        dmc.Card(
                                                children=[
                                                    dmc.CardSection(
                                                        dmc.Group(
                                                            children=[
                                                                dmc.Text(etapasdetailIA_header_graph["result2"], 
                                                                    weight=500,
                                                                    variant="gradient",
                                                                    gradient={"from": "blue", "to": "fuchsia", "deg": 100},
                                                                    style={"fontSize": 20},
                                                                ),                                                                
                                                            ],
                                                            position="apart",
                                                        ),
                                                        withBorder=True,
                                                        inheritPadding=True,
                                                        py="xs",
                                                    ),
                                                    dmc.Text(
                                                        children=[
                                                            dmc.Text(etapasdetailIA_header_graph["detail2"],
                                                            )
                                                        ],
                                                        mt="sm",
                                                        color="dimmed",
                                                        size="sm",
                                                    ),
                                                    dmc.CardSection(
                                                        dmc.Image(
                                                            src=app.get_asset_url("data_engineering.png"),
                                                            mt="sm",
                                                        ),
                                                    ),                                                    
                                                ],
                                                withBorder=True,
                                                shadow="sm",
                                                radius="lg",
                                                #style={"width": 1000},
                                            ),
                                         width={"size": 6, "offset": 1}
                                    ),
                                ]
                            ),    
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            dbc.Row(
                                 children=[
                                    dbc.Col(
                                        html.Div(
                                            children=[
                                                html.Div(
                                                     dmc.Badge(
                                                        "3. Generación",
                                                        variant="gradient",
                                                        gradient={"from": "grape", "to": "pink", "deg": 35},
                                                        id="generacion", 
                                                        size="xl",
                                                    ),                                                   
                                                ),                                                 
                                                html.Br(),
                                                dmc.Text(
                                                    etapasdetailIA[3],                                                
                                                    variant="gradient",
                                                    gradient={"from": "skyblue", "to": "fuchsia", "deg": 100},
                                                    style={"fontSize": 20},
                                                ),                                                 
                                            ],                                                                                    
                                        ),
                                        width=4,
                                        align = "top",
                                        style={'text-align': 'right'},
                                    ),
                                    dbc.Col(
                                        dmc.Card(
                                                children=[
                                                    dmc.CardSection(
                                                        dmc.Group(
                                                            children=[
                                                                dmc.Text(etapasdetailIA_header_graph["result3"], 
                                                                    weight=500,
                                                                    variant="gradient",
                                                                    gradient={"from": "blue", "to": "fuchsia", "deg": 100},
                                                                    style={"fontSize": 20},
                                                                ),                                                                
                                                            ],
                                                            position="apart",
                                                        ),
                                                        withBorder=True,
                                                        inheritPadding=True,
                                                        py="xs",
                                                    ),
                                                    dmc.Text(
                                                        children=[
                                                            dmc.Text(etapasdetailIA_header_graph["detail3"],
                                                            )
                                                        ],
                                                        mt="sm",
                                                        color="dimmed",
                                                        size="sm",
                                                    ),
                                                    dmc.CardSection(
                                                        dmc.Image(
                                                            src=app.get_asset_url("generacion.png"),
                                                            mt="sm",
                                                        ),
                                                    ),                                                    
                                                ],
                                                withBorder=True,
                                                shadow="sm",
                                                radius="lg",
                                                #style={"width": 1000},
                                            ),
                                         width={"size": 6, "offset": 1}
                                    ),
                                ]
                            ),    
                            html.Br(),
                            html.Br(),
                            html.Br(), 
                            dbc.Row(
                              children=[ 
                                    dbc.Col(
                                        html.Div(
                                            children=[
                                                html.Div(
                                                     dmc.Badge(
                                                        "4. Producción",
                                                        variant="gradient",
                                                        gradient={"from": "grape", "to": "pink", "deg": 35},
                                                        id="produccion", 
                                                        size="xl",
                                                    ),                                                   
                                                ),                                                 
                                                html.Br(),
                                                dmc.Text(
                                                    etapasdetailIA[4],                                                
                                                    variant="gradient",
                                                    gradient={"from": "skyblue", "to": "fuchsia", "deg": 100},
                                                    style={"fontSize": 20},
                                                ),                                                 
                                            ],                                                                                    
                                        ),
                                        width=4,
                                        align = "top",
                                        style={'text-align': 'right'},
                                    ),
                                    dbc.Col(
                                        dmc.Card(
                                                children=[
                                                    dmc.CardSection(
                                                        dmc.Group(
                                                            children=[
                                                                dmc.Text(etapasdetailIA_header_graph["result4"], 
                                                                    weight=500,
                                                                    variant="gradient",
                                                                    gradient={"from": "blue", "to": "fuchsia", "deg": 100},
                                                                    style={"fontSize": 20},
                                                                ),                                                                
                                                            ],
                                                            position="apart",
                                                        ),
                                                        withBorder=True,
                                                        inheritPadding=True,
                                                        py="xs",
                                                    ),
                                                    dmc.Text(
                                                        children=[
                                                            dmc.Text(etapasdetailIA_header_graph["detail4"],
                                                            )
                                                        ],
                                                        mt="sm",
                                                        color="dimmed",
                                                        size="sm",
                                                    ),
                                                    dmc.CardSection(
                                                        dmc.Image(
                                                            src=app.get_asset_url("produccion.jpg"),
                                                            mt="sm",
                                                        ),
                                                    ),                                                    
                                                ],
                                                withBorder=True,
                                                shadow="sm",
                                                radius="lg",
                                                #style={"width": 1000},
                                            ),
                                         width={"size": 6, "offset": 1}
                                    ),
                                ]
                            ),    
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            dbc.Row(
                                children=[ 
                                    dbc.Col(
                                        html.Div(
                                            children=[
                                                html.Div(
                                                    dmc.Badge(
                                                        "5. Mejora",
                                                        variant="gradient",
                                                        gradient={"from": "grape", "to": "pink", "deg": 35},
                                                        id="mejora", 
                                                        size="xl",
                                                        ),                                                   
                                                    ),                                                 
                                                    html.Br(),
                                                    dmc.Text(
                                                        etapasdetailIA[5],                                                
                                                        variant="gradient",
                                                        gradient={"from": "skyblue", "to": "fuchsia", "deg": 100},
                                                        style={"fontSize": 20},
                                                    ),                                                 
                                                ],                                                                                    
                                            ),
                                        width=4,
                                        align = "top",
                                        style={'text-align': 'right'},
                                    ),
                                    dbc.Col(
                                        dmc.Card(
                                                children=[
                                                    dmc.CardSection(
                                                        dmc.Group(
                                                            children=[
                                                                dmc.Text(etapasdetailIA_header_graph["result5"], 
                                                                    weight=500,
                                                                    variant="gradient",
                                                                    gradient={"from": "blue", "to": "fuchsia", "deg": 100},
                                                                    style={"fontSize": 20},
                                                                ),                                                                
                                                            ],
                                                            position="apart",
                                                        ),
                                                        withBorder=True,
                                                        inheritPadding=True,
                                                        py="xs",
                                                    ),
                                                    dmc.Text(
                                                        children=[
                                                            dmc.Text(etapasdetailIA_header_graph["detail5"],
                                                            )
                                                        ],
                                                        mt="sm",
                                                        color="dimmed",
                                                        size="sm",
                                                    ),
                                                    dmc.CardSection(
                                                        dmc.Image(
                                                            src=app.get_asset_url("mejora.jpg"),
                                                            mt="sm",
                                                        ),
                                                    ),                                                    
                                                ],
                                                withBorder=True,
                                                shadow="sm",
                                                radius="lg",
                                                #style={"width": 1000},
                                            ),
                                         width={"size": 6, "offset": 1}
                                    ),
                                ]
                            ),    
                            html.Br(),
                            html.Br(),
                            html.Br(),                              
                        ]
                    )                
                ),
                html.Br(),
                html.Br(),
                # Last words                
                dbc.Row(
                    [
                        dbc.Col(html.Div("One of three columns"),
                        align = "center",  
                        style={'text-align': 'right'},                      
                        ),
                        dbc.Col(html.Div("One of three columns"),
                        align = "center",  
                        style={'text-align': 'center'},                             
                        ),
                        dbc.Col(html.Div("One of three columns"),
                        align = "center",
                        style={'text-align': 'left'},
                        ),
                    ],
                    className="g-0",
                ),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),   
                # Credits ----
                 dbc.Row(
                    creditos,                    
                    justify="center",
                ),                                         
                # Foot ----
                dbc.Row(
                    pie,                    
                    justify="center",
                ),                  
            ]        
        ),
    ]
    