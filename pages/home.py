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
                # Carrusel y primera frase ----
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
                                                "border-radius": "400px",
                                                "background-color": "rgba(0,0,0,0)",
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
                                        "Multiplo es un empresa dedicada a mejorar procesos empresariales aplicando Inteligencia Artificial (IA). De datos caóticos a nuevos productos, brindamos herramientas avanzadas para mejorar los márgenes y la rentabilidad del negocio.",
                                        variant="gradient",
                                        gradient={"from": "skyblue", "to": "fuchsia", "deg": 100},
                                        style={"fontSize": 40},
                                    ),
                                    html.Br(),
                                    dmc.Text(
                                        "¿Tenes datos? Multiplo se ocupa del conocimiento.",                                        
                                        color="gray",
                                        style={"fontSize": 30},
                                    ),
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
                # Contacto ----
                dbc.Row(
                    html.Div(
                        [
                            dbc.Button("Conocer nuestras soluciones", outline=True, color="primary"),
                            dbc.Button("Comunicarse con ventas", outline=True, color="secondary"),
                        ],
                        className="d-grid gap-2 col-2 mx-auto lg-1",                        
                    )
                ),                
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
                                                "Multiplo te acompaña para incoporar IA en la empresa",
                                                variant="gradient",
                                                gradient={"from": "fuchsia", "to": "skyblue", "deg": 100},
                                                style={"fontSize": 40},
                                            ),
                                            html.Br(),
                                            dmc.Text(
                                                "En este proyeto cada etapa es una unidad que genera resultados de valor",                                        
                                                color="gray",
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
                                          gif.GifPlayer(
                                            gif='assets/liguid4.gif',
                                            still='assets/liguid4.gif',
                                            autoplay = True,
                                            ),
                                        id="liq1",
                                    ),  
                                    dbc.Tooltip(
                                            "Planillas, documentos, BDs, otras fuentes",
                                            target="liq1",
                                            placement = "top",
                                    ),
                                    html.Br(),                                  
                                    dmc.Group(
                                        [
                                            dmc.Badge("Inicio", variant="gradient"),
                                            dbc.Button("1. Acceso a Datos", 
                                                outline=True, 
                                                color="light",
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
                                                "A partir de los objetivos de la organización se inicia un proyecto de implementación de IA identificando la información disponible y su estado.",
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
                                          gif.GifPlayer(
                                            gif='assets/liguid2.gif',
                                            still='assets/liguid2.gif',
                                            autoplay = True,
                                            ),
                                        id="liq2",
                                    ),
                                    dbc.Tooltip(
                                            "Nuevos datos, relaciones, patrones y tendencias",
                                            target="liq2",
                                            placement = "top",
                                    ),
                                    html.Br(),
                                    dmc.Group(
                                        [
                                            #dmc.Text("Norway Fjord Adventures", weight=500),
                                            #dmc.Badge("Integración", color="gray", variant="dark"),
                                            dbc.Button("2. Ingeniería de Datos", 
                                                outline=True, 
                                                color="light",
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
                                                "De los datos disponible inferimos patrones y relaciones que permitirán modelar el problema en estudio y crear soluciones novedosas.",
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
                                          gif.GifPlayer(
                                            gif='assets/liguid5.gif',
                                            still='assets/liguid5.gif',
                                            autoplay = True,
                                            ),
                                        id="liq3",
                                    ),
                                    dbc.Tooltip(
                                            "Modelos, proyecciones y predicciones",
                                            target="liq3",
                                            placement = "top",
                                    ),
                                    html.Br(),
                                    dmc.Group(
                                        [
                                            #dmc.Text("Norway Fjord Adventures", weight=500),
                                            #dmc.Badge("Integración", color="gray", variant="dark"),
                                            dbc.Button("3. Generación de Modelos", 
                                                outline=True, 
                                                color="light",
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
                                                "Empleando aprendizaje automático (algorítimico) y optimización se aislan las soluciones más efectivas y redituables para la organización.",
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
                                          gif.GifPlayer(
                                            gif='assets/liguid3.gif',
                                            still='assets/liguid3.gif',
                                            autoplay = True,                                            
                                            ),
                                        id="liq4",
                                    ),
                                    dbc.Tooltip(
                                            "Aplicación Web para consulta, APIs, Reportes, otros",
                                            target="liq4",
                                            placement = "top",
                                    ),
                                    html.Br(),
                                    dmc.Group(
                                        [
                                            #dmc.Text("Norway Fjord Adventures", weight=500),
                                            #dmc.Badge("Integración", color="gray", variant="dark"),
                                            dbc.Button("4. Puesta en Producción", 
                                                outline=True,                                                 
                                                color="light",
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
                                                "Creamos el contexto tecnológico necesario para aplicar las soluciones y modelos generados al trabajo cotidiano de la empresa.",
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
                                            gif.GifPlayer(
                                                gif='assets/liguid1.gif',
                                                still='assets/liguid1.gif',
                                                autoplay = True,
                                                ),
                                            id="liq5",
                                        ),
                                        dbc.Tooltip(
                                                "Incoporación de mejoras y desarrollo de herramientas",
                                                target="liq5",
                                                placement = "top",
                                        ),
                                        html.Br(),
                                        dmc.Group(
                                            [
                                                #dmc.Text("Norway Fjord Adventures", weight=500),
                                                #dmc.Badge("Integración", color="gray", variant="dark"),
                                                dbc.Button("5. Control y Mejora", 
                                                    outline=True, 
                                                    color="light",
                                                    size="lg",
                                                    #disabled=True,
                                                ),
                                                dmc.Badge("Fin", variant="gradient"),
                                            ],
                                            position="center",
                                            mt="md",
                                            mb="xs",
                                        ),
                                        html.Br(),
                                        dmc.Center(
                                            children=[
                                                dmc.Text(
                                                    "Supervisamos el desempeño de los modelos, verificando la conformidad de sus resultados a los objetivos y criterios de la empresa.",
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
    