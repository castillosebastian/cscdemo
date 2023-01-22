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

geometry_main = app.get_asset_url("geometry_main.gif")

img_style = {"height": "400px", "width": "700px"}

carrusel = [
    {"key": "1", "src": "/assets/im4_edited.png"},
    {"key": "2", "src": "/assets/im1_edited.png"},    
    {"key": "4", "src": "/assets/im2_edited.png"},
    {"key": "5", "src": "/assets/im3_edited.png"},
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


def layout():
    return [
        html.Div(            
            [     
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
                            width=6,
                            ),
                            dbc.Col(html.Div(
                                dcc.Markdown('''
                                    >
                                    > 
                                    > Multiplo es un empresa dedicada a mejorar procesos
                                    > aplicando *Inteligencia Artificial* a tareas humanas
                                    > [->](/multiplo)
                                    >                                    
                                    '''
                                ),                                
                                style = {
                                    "font-size": 40,
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
                dbc.Row(

                    html.Div(
                        [
                            dbc.Row(
                                [
                                    #dbc.Col(dbc.Card(problemas, color="primary", inverse=True)),
                                    dbc.Col(dbc.Card(problemas, color="dark", inverse=True)),
                                    dbc.Col(dbc.Card(problemas, color="info", inverse=True)),
                                ],
                                className="mb-4",
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(dbc.Card(problemas, color="success", inverse=True)),
                                    dbc.Col(dbc.Card(problemas, color="warning", inverse=True)),
                                    dbc.Col(dbc.Card(problemas, color="danger", inverse=True)),
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
                dbc.Col(html.Div(
                                dcc.Markdown('''
                                    >
                                    > 
                                    > Multiplo es un empresa dedicada a mejorar procesos",
                                    > mediante la incorporación de *Inteligencia Artificial*",                                    
                                    > en las tareas de las organizaciones.
                                    > [Ver nuestra metodología de trabajo](/multiplo)
                                    >                                    
                                    '''
                                ),
                                style = {
                                    "font-size": 40,
                                },
                            ),
                            #widht = 10,
                            align = "center", 
                        ),          
                dbc.Row(                                       
                        children=[
                            dbc.Col(html.Div(
                                [
                                    
                                    ]
                                ),
                                width=4,
                            ),
                            dbc.Col(
                                dbc.Card(
                                    dbc.CardBody(
                                        children=[
                                            dbc.CardHeader("Datos dispersos y heterogéneos"),
                                            html.P(
                                                "This is a wider card with supporting text "
                                                "below as a natural lead-in to additional "
                                                "content. This content is a bit longer.",                                                    
                                            ),
                                        ]
                                    )
                                ),
                            width=8,
                        ),
                    ],
                ),
                dbc.Row(                                       
                        children=[
                            dbc.Col(html.Div(
                                [
                                   
                                    ]
                                ),
                                width=4,
                            ),
                            dbc.Col(
                                dbc.Card(
                                    dbc.CardBody(
                                        children=[
                                            dbc.CardHeader("Datos dispersos y heterogéneos"),
                                            html.P(
                                                "This is a wider card with supporting text "
                                                "below as a natural lead-in to additional "
                                                "content. This content is a bit longer.",                                                    
                                            ),
                                        ]
                                    )
                                ),
                            width=8,
                        ),
                    ],
                ),
            ]),
        ]
    