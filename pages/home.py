import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
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


img_style = {"height": "250px", "width": "450px"}

carrusel = [
    {"key": "1", "src": "/assets/im3_1_edited.png"},
    {"key": "2", "src": "/assets/im3_2_edited.png"},    
    {"key": "3", "src": "/assets/im3_3_edited.png"},    
    ]

problemas = [
    dbc.CardHeader("Card header"),
    dbc.CardBody(
        [
            html.H5("Card title", className="card-title"),
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",
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
                                        controls=False,
                                        indicators=True,
                                        interval=4000,
                                        style = img_style,
                                        #ride="carousel",
                                    )
                                ]                                    
                            ),
                            width=4,
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
    