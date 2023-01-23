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
                # Carrusel y primera frase ----
                dbc.Row(                                       
                        children=[
                            dbc.Col(html.Div(
                                [
                                     dbc.Carousel(
                                        items= carrusel,                                       
                                        class_name="carousel-fade",
                                        controls=True,
                                        indicators=True,
                                        interval=3000,
                                        variant="dark",
                                        #ride="carousel",
                                    )
                                ]                                    
                            ),
                            width=6,
                            ),
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
                                    "font-size": 30,
                                },
                            ),
                            width=6,
                        )
                    ],
                    align = "center", 
                    ),                
                html.Br(),
                html.Br(),                
                # Contacto ----
                dbc.Row(
                    html.Div(
                        [
                            dbc.Button("Conocer nuestras soluciones", outline=True, color="primary", className="me-1"),
                            dbc.Button("Comunicarse con ventas", outline=True, color="secondary", className="me-1"),
                        ],
                        className="d-grid gap-2 d-md-block",
                    )
                ),                
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                # ML Pipeline ----
                html.Div(
                    [
                        dbc.Button("Pasos de un Proyecto Analítico", 
                        outline=True, 
                        color="light",
                        disabled=True,
                        ),
                    ],
                    className="d-grid gap-2",
                ),
                html.Br(),                
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
                                            )
                                    ),
                                    dmc.Group(
                                        [
                                            #dmc.Text("Norway Fjord Adventures", weight=500),
                                            #dmc.Badge("Integración", color="gray", variant="dark"),
                                            dbc.Button("Integración", 
                                                outline=True, 
                                                color="light",
                                                disabled=True,
                                                ),
                                        ],
                                        position="center",
                                        mt="md",
                                        mb="xs",
                                    ),
                                    dmc.Center(
                                        children=[
                                            dmc.Text(
                                        "With Fjord Tours you can explore more of the magical fjord landscapes with tours and activities on and around the fjords of Norway",
                                        size="sm",
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
                                            )
                                    ),
                                    dmc.Group(
                                        [
                                            #dmc.Text("Norway Fjord Adventures", weight=500),
                                            #dmc.Badge("Integración", color="gray", variant="dark"),
                                            dbc.Button("Integración", 
                                                outline=True, 
                                                color="light",
                                                disabled=True,
                                                ),
                                        ],
                                        position="center",
                                        mt="md",
                                        mb="xs",
                                    ),
                                    dmc.Center(
                                        children=[
                                            dmc.Text(
                                        "With Fjord Tours you can explore more of the magical fjord landscapes with tours and activities on and around the fjords of Norway",
                                        size="sm",
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
                                            )
                                    ),
                                    dmc.Group(
                                        [
                                            #dmc.Text("Norway Fjord Adventures", weight=500),
                                            #dmc.Badge("Integración", color="gray", variant="dark"),
                                            dbc.Button("Integración", 
                                                outline=True, 
                                                color="light",
                                                disabled=True,
                                                ),
                                        ],
                                        position="center",
                                        mt="md",
                                        mb="xs",
                                    ),
                                    dmc.Center(
                                        children=[
                                            dmc.Text(
                                        "With Fjord Tours you can explore more of the magical fjord landscapes with tours and activities on and around the fjords of Norway",
                                        size="sm",
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
                                            )
                                    ),
                                    dmc.Group(
                                        [
                                            #dmc.Text("Norway Fjord Adventures", weight=500),
                                            #dmc.Badge("Integración", color="gray", variant="dark"),
                                            dbc.Button("Integración", 
                                                outline=True, 
                                                color="light",
                                                disabled=True,
                                                ),
                                        ],
                                        position="center",
                                        mt="md",
                                        mb="xs",
                                    ),
                                    dmc.Center(
                                        children=[
                                            dmc.Text(
                                        "With Fjord Tours you can explore more of the magical fjord landscapes with tours and activities on and around the fjords of Norway",
                                        size="sm",
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
                                            )
                                    ),
                                    dmc.Group(
                                        [
                                            #dmc.Text("Norway Fjord Adventures", weight=500),
                                            #dmc.Badge("Integración", color="gray", variant="dark"),
                                            dbc.Button("Integración", 
                                                outline=True, 
                                                color="light",
                                                disabled=True,
                                                ),
                                        ],
                                        position="center",
                                        mt="md",
                                        mb="xs",
                                    ),
                                    dmc.Center(
                                        children=[
                                            dmc.Text(
                                        "With Fjord Tours you can explore more of the magical fjord landscapes with tours and activities on and around the fjords of Norway",
                                        size="sm",
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
                # Stages ----
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
                # Creditos ----
                 dbc.Row(
                    creditos,                    
                    justify="center",
                ),                                         
                # Final home ----
                dbc.Row(
                    pie,                    
                    justify="center",
                ),                  
            ]        
        ),
    ]
    