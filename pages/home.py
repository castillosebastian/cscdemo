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
#import dash_twitter_widget

from app import app
from data_reader import *
from pages.constructors import constructor_standings_by_year

URL_seasons = "http://ergast.com/api/f1/seasons.json?limit=80"

data_seasons = requests.get(url=URL_seasons).json()

season_list = []
for year in data_seasons["MRData"]["SeasonTable"]["Seasons"]:
    season_list.append(year["season"])

season_list.reverse()

df_races_test = df_races.rename(columns={"name": "race_name", "url": "race_url"})
df_homepage_constructors = constructor_standings_by_year(2020)


def generate_recent_driver_standings():
    merge_standings = pd.merge(
        df_drivers, df_driver_standings, how="inner", on=["driverId"]
    )

    merge_standings_races = pd.merge(
        merge_standings, df_races_test, how="inner", on=["raceId"]
    )

    merge_standings_races_filtered = merge_standings_races[
        [
            "forename",
            "surname",
            "nationality",
            "points",
            "positionText",
            "wins",
            "year",
            "round",
        ]
    ]

    standings_all_rounds = merge_standings_races_filtered[
        (merge_standings_races_filtered["year"] == 2020)
    ].sort_values(by=["round", "points"], ascending=False)
    standings_all_rounds["driverName"] = (
        standings_all_rounds["forename"].astype(str)
        + " "
        + standings_all_rounds["surname"]
    )
    final_round = standings_all_rounds["round"].max()
    standings_final_round = standings_all_rounds[
        standings_all_rounds["round"] == final_round
    ]
    standings_final_round = standings_final_round[
        ["positionText", "driverName", "nationality", "points", "wins"]
    ]

    standings_final_round = standings_final_round.rename(
        columns={
            "driverName": "Name",
            "nationality": "Nationality",
            "points": "Points",
            "positionText": "Rank",
            "wins": "Wins",
            "year": "Year",
        }
    )
    return standings_final_round


df_homepage_drivers = generate_recent_driver_standings()


def layout():
    return [    
        html.Div(
            children=[
                dbc.Card(
                    [
                        dbc.Card(
                            children=[
                                dbc.CardHeader("Inicio"),
                                dbc.CardBody(
                                    children=[
                                        dcc.Markdown(
                                            """
                                            ...
                                            """,
                                            style={"margin": "0 10px"},
                                        ),
                                    ]
                                )
                            ]
                        ),                        
                        dbc.Card(
                            children=[
                                dbc.CardHeader("Pilotos"),
                                dbc.CardBody(
                                    children=[
                                        dbc.Table.from_dataframe(
                                            df_homepage_drivers, 
                                            striped=True, 
                                            bordered=True, 
                                            hover=True
                                        )                                        
                                    ]
                                ),
                            ]
                        ),
                        dbc.Card(
                            children=[
                                dbc.CardHeader("Escuderías"),
                                dbc.CardBody(
                                    children=[
                                        dbc.Table.from_dataframe(
                                            df_homepage_constructors, 
                                            striped=True, 
                                            bordered=True, 
                                            hover=True
                                        )
                                    ]
                                ),
                            ]
                        ),
                    ]
                )
            ],            
        ),
    ]

