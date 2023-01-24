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

problemas = [
    dbc.CardHeader("Card header"),
    dbc.CardBody(
        [
            #html.H5("Card title", className="card-title"),
            html.P(
                dcc.Markdown('''
                Multiplo es un empresa dedicada a mejorar procesos
                aplicando *Inteligencia Artificial* en tareas humanas.
                Multiplo es un empresa dedicada a mejorar procesos
                aplicando *Inteligencia Artificial* en tareas humanas.
                Multiplo es un empresa dedicada a mejorar procesos
                aplicando *Inteligencia Artificial* en tareas humanas.
                Multiplo es un empresa dedicada a mejorar procesos
                aplicando *Inteligencia Artificial* en tareas humanas.
                Multiplo es un empresa dedicada a mejorar procesos
                aplicando *Inteligencia Artificial* en tareas humanas.
                Multiplo es un empresa dedicada a mejorar procesos
                aplicando *Inteligencia Artificial* en tareas humanas.
                Multiplo es un empresa dedicada a mejorar procesos
                aplicando *Inteligencia Artificial* en tareas humanas.
                Multiplo es un empresa dedicada a mejorar procesos
                aplicando *Inteligencia Artificial* en tareas humanas.
                [(ver)](/multiplo)                                                  
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

size_texto_cuerpo = 20

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
                                        "Multiplo es un empresa dedicada a mejorar procesos empresariales aplicando Inteligencia Artificial (IA). De datos caóticos a nuevos productos, brindamos sistemas avanzados para mejorar los márgenes y la rentabilidad del negocio.",
                                        variant="gradient",
                                        gradient={"from": "skyblue", "to": "fuchsia", "deg": 100},
                                        style={"fontSize": 30},
                                    ),
                                    html.Br(),
                                    html.Br(),
                                    dmc.Text(
                                        "¿Tenes datos? Multiplo se ocupa del conocimiento.",                                        
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
                                            dmc.Badge(
                                                "Inicio", 
                                                variant="gradient",
                                                gradient={"from": "grape", "to": "pink", "deg": 35},
                                            ),
                                            dbc.Button("1. Acceso", 
                                                outline=True, 
                                                color="info",
                                                size="lg",                                                
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
                                                "A partir de los objetivos de la organización se inicia un proyecto de implementación de IA identificando el estado tecnológico de la empresa y la información disponible.",
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
                                                size="lg",
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
                                                "Con los datos disponible investigamos patrones y relaciones que permitirán modelar el problema atacado y crear soluciones novedosas.",
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
                                            src= app.get_asset_url("settings-sliders.png"),                                            
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
                                                size="lg",
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
                                                "Empleando IA se aislan las soluciones más efectivas, optimizando su configuración hasta lograr los estándares fijados por la empresa.",
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
                                                size="lg",
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
                                                "Generamos la infraestructura tecnológica necesaria para aplicar las soluciones creadas a las tareas cotidianas de la empresa. El foco está puesto en la robustez y usabilidad.",
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
                                                src= app.get_asset_url("search-analysis.png"),                                            
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
                                                #dmc.Text("Norway Fjord Adventures", weight=500),
                                                #dmc.Badge("Integración", color="gray", variant="dark"),
                                                dbc.Button("5. Mejora", 
                                                    outline=True, 
                                                    color="info",
                                                    size="lg",
                                                    #disabled=True,
                                                ),
                                                 dmc.Badge(
                                                    "Fin", 
                                                    variant="gradient",
                                                    gradient={"from": "grape", "to": "pink", "deg": 35},
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
                                                    "Controlamos el desempeño de los modelos, verificando su conformidad a los objetivos de la empresa, buscando oportunidades de mejorar sus resultados.",
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
                                    dbc.Col(html.Div(
                                        dcc.Markdown('''
                                            >
                                            > 
                                            > Multiplo es un empresa dedicada a mejorar procesos
                                            > aplicando *Inteligencia Artificial* en tareas humanas.
                                            > [(ver)](/multiplo)
                                            >                                    
                                            '''
                                        ),                                
                                        style = {
                                            "font-size": 20,
                                        },
                                        ),
                                        width=4,
                                        align = "center",
                                        style={'text-align': 'right'},
                                    ),
                                    dbc.Col(
                                        dbc.Card(
                                        problemas, 
                                        #color="info",  
                                        #outline=True,
                                        className="border-0 bg-transparent",
                                        ),
                                        width=8,
                                    ),
                                ]
                            ),    
                            html.Br(),
                            html.Br(),
                            html.Br(), 
                            dbc.Row(
                                children=[                                    
                                    dbc.Col(html.Div(
                                        dcc.Markdown('''
                                            >
                                            > 
                                            > Multiplo es un empresa dedicada a mejorar procesos
                                            > aplicando *Inteligencia Artificial* en tareas humanas.
                                            > [(ver)](/multiplo)
                                            >                                    
                                            '''
                                        ),                                
                                        style = {
                                            "font-size": 20,
                                        },
                                        ),
                                        width=4,
                                        align = "center",
                                        style={'text-align': 'right'},
                                    ),
                                    dbc.Col(
                                        dbc.Card(
                                        problemas, 
                                        #color="info",  
                                        #outline=True,
                                        className="border-0 bg-transparent",
                                        ),
                                        width=8,
                                    ),
                                ]
                            ),    
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            dbc.Row(
                                children=[                                    
                                    dbc.Col(html.Div(
                                        dcc.Markdown('''
                                            >
                                            > 
                                            > Multiplo es un empresa dedicada a mejorar procesos
                                            > aplicando *Inteligencia Artificial* en tareas humanas.
                                            > [(ver)](/multiplo)
                                            >                                    
                                            '''
                                        ),                                
                                        style = {
                                            "font-size": 20,
                                        },
                                        ),
                                        width=4,
                                        align = "center",
                                        style={'text-align': 'right'},
                                    ),
                                    dbc.Col(
                                        dbc.Card(
                                        problemas, 
                                        #color="info",  
                                        #outline=True,
                                        className="border-0 bg-transparent",
                                        ),
                                        width=8,
                                    ),
                                ]
                            ),    
                            html.Br(),
                            html.Br(),
                            html.Br(), 
                            dbc.Row(
                                children=[                                    
                                    dbc.Col(html.Div(
                                        dcc.Markdown('''
                                            >
                                            > 
                                            > Multiplo es un empresa dedicada a mejorar procesos
                                            > aplicando *Inteligencia Artificial* en tareas humanas.
                                            > [(ver)](/multiplo)
                                            >                                    
                                            '''
                                        ),                                
                                        style = {
                                            "font-size": 20,
                                        },
                                        ),
                                        width=4,
                                        align = "center",
                                        style={'text-align': 'right'},
                                    ),
                                    dbc.Col(
                                        dbc.Card(
                                        problemas, 
                                        #color="info",  
                                        #outline=True,
                                        className="border-0 bg-transparent",
                                        ),
                                         width=8,
                                    ),
                                ]
                            ),    
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            dbc.Row(
                                children=[                                    
                                    dbc.Col(html.Div(
                                        dcc.Markdown('''
                                            >
                                            > 
                                            > Multiplo es un empresa dedicada a mejorar procesos
                                            > aplicando *Inteligencia Artificial* en tareas humanas.
                                            > [(ver)](/multiplo)
                                            >                                    
                                            '''
                                        ),                                
                                        style = {
                                            "font-size": 20,
                                        },
                                        ),
                                        width=4,
                                        align = "center",
                                        style={'text-align': 'right'},
                                    ),
                                    dbc.Col(
                                        dbc.Card(
                                        problemas, 
                                        #color="info",  
                                        #outline=True,
                                        className="border-0 bg-transparent",
                                        ),
                                         width=8,
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
    