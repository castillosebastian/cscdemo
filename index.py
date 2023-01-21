from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from dash import dash_table
from dash.exceptions import PreventUpdate
import pandas as pd
import plotly.graph_objs as go
import os
import pandas as pd
from dash.dependencies import Input, Output, State
from app import app
import pages
from dash_bootstrap_templates import load_figure_template
load_figure_template("vapor")

SIDEBAR_STYLE = {
    #"position": "fixed",
    "top": 2,
    "left": 10,
    "bottom": 0,
    "width": "150rem",
    "padding": "2rem 1rem",
    "font-size": "0.9cm",
    #"background-color": "#878f99",
}

CONTENT_STYLE = {
    "margin-left": "5rem",
    "margin-right": "3rem",
    "padding": "2rem 1rem",
}
server = app.server

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),

        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Inicio", href=app.get_relative_path("/"))),
                dbc.NavItem(dbc.NavLink("Seasons", href=app.get_relative_path("/seasons"))),
                dbc.NavItem(dbc.NavLink("Constructors", href=app.get_relative_path("/constructors"))),
                dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem("Mas", header=True),                        
                        dbc.DropdownMenuItem("Circuits", href=app.get_relative_path("/circuits")),
                    ],
                    nav=True,
                    in_navbar=True,
                    label="Mas",
                ),
            ],
            brand="Multiplo",
            brand_href=app.get_relative_path("/"),
            color="primary",
            dark=True,
        ),        
        html.Div(id="page-content", style=CONTENT_STYLE),
    ]
)

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page_content(pathname):
    path = app.strip_relative_path(pathname)
    if not path:
        return pages.home.layout()
    elif path == "seasons":
        return pages.seasons.layout()
    elif path == "circuits":
        return pages.circuits.layout()
    elif path == "drivers":
        return pages.drivers.layout()
    elif path == "constructors":
        return pages.constructors.layout()
    else:
        return "404"


if __name__ == "__main__":
    app.run_server(debug=True)
