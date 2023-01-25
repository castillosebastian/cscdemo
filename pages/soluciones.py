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
                                         dmc.Text("algo")
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
                                                    "Algo",                                                
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
                                                                dmc.Text("algo", 
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
                                                                "algo",
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
                # Foot ----
                dbc.Row(
                    dmc.Text("algo"),                    
                    justify="center",
                ),                  
            ]        
        ),
    ]
    