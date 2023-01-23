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
                                        interval=4000,
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
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                # Contacto ----
                dbc.Row(
                    html.Div(
                        [
                            dbc.Button("Conocer nuestras soluciones", color="primary"),
                            dbc.Button("Comunicarse con ventas", color="secondary"),
                        ],
                        className="d-grid gap-2 col-6 mx-auto",
                    )
                ),                
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                # Presentación ----
                dbc.Row(
                    html.Div(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(dbc.Card(
                                        problemas, 
                                        color="primary", 
                                        outline=True,
                                        className="border-1 bg-transparent",
                                        )),
                                    dbc.Col(dbc.Card(
                                        problemas, 
                                        color="dark", 
                                        outline=True,
                                        className="border-1 bg-transparent",
                                        )),
                                    dbc.Col(dbc.Card(
                                        problemas, 
                                        color="info", 
                                        outline=True,
                                        className="border-1 bg-transparent",                                    
                                    )),
                                ],
                                className="mb-4",
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(dbc.Card(
                                        problemas, 
                                        color="success", 
                                        outline=True,
                                        className="border-1 bg-transparent",
                                        )),
                                    dbc.Col(dbc.Card(
                                        problemas, 
                                        color="warning", 
                                        outline=True,
                                        className="border-1 bg-transparent",
                                        )),
                                    dbc.Col(dbc.Card(
                                        problemas, 
                                        color="danger", 
                                        outline=True,
                                        className="border-1 bg-transparent",
                                        )),                                    
                                ],
                                className="mb-4",
                            ),
                        ]
                    )                
                ),
                html.Br(),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(
                            dmc.Card(
                                children=[
                                    dmc.CardSection(
                                        dmc.Image(
                                            src="https://images.unsplash.com/photo-1527004013197-933c4bb611b3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=720&q=80",
                                            height=160,
                                        )
                                    ),
                                    dmc.Group(
                                        [
                                            dmc.Text("Norway Fjord Adventures", weight=500),
                                            dmc.Badge("On Sale", color="red", variant="light"),
                                        ],
                                        position="apart",
                                        mt="md",
                                        mb="xs",
                                    ),
                                    dmc.Text(
                                        "With Fjord Tours you can explore more of the magical fjord landscapes with tours and activities on and around the fjords of Norway",
                                        size="sm",
                                        color="dimmed",
                                    ),
                                    dmc.Button(
                                        "Book classic tour now",
                                        variant="light",
                                        color="blue",
                                        fullWidth=True,
                                        mt="md",
                                        radius="md",
                                    ),
                                ],
                                withBorder=True,
                                shadow="sm",
                                radius="md",
                                style={"width": 350},
                            )),
                        dbc.Col(
                            html.Div("One of three columns"),
                            align = "center",
                            style={'text-align': 'center'},),
                        dbc.Col(
                            html.Div("One of three columns"),
                            align = "center",
                            style={'text-align': 'center'},),
                        dbc.Col(
                            html.Div("One of three columns"),
                            align = "center",
                            style={'text-align': 'center'},),
                        dbc.Col(
                            html.Div("One of three columns"),
                            align = "center",
                            style={'text-align': 'center'},),
                    ]
                ),
                html.Br(),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(html.Div("One of three columns"),
                        align = "center",  
                        style={'text-align': 'right'},                      
                        ),
                        dbc.Col(html.Div(
                            dbc.Col(
                                    gif.GifPlayer(
                                        gif='assets/unrelatedpoints.gif',
                                        still='assets/unrelatedpoints.gif',
                                        autoplay = True,
                                    )
                                ),
                            )),
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
                # Final home ----
                dbc.Row(
                    pie,
                    justify="center",
                ),                  
            ]        
        ),
    ]
    