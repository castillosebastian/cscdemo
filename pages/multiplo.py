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
import dash_gif_component as gif
from app import app

def layout():
    return [
        html.Div(            
            [                
                dbc.Row(                                       
                        children=[
                            dbc.Col(html.Div([
                                        gif.GifPlayer(
                                                gif='assets/geometry0.gif',
                                                still='assets/geometry0.gif',
                                                autoplay = True,
                                            )
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
                )
            ]),
        ]
    