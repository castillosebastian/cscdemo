import dash
from dash import dcc
from dash import html
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

SIDEBAR_STYLE = {
    #"position": "fixed",
    "top": 2,
    "left": 10,
    "bottom": 0,
    "width": "150rem",
    "padding": "2rem 1rem",
    "font-size": "0.8cm",
    "background-color": "#878f99",
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
        dbc.Navbar(
            children=[
                html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Img(
                                    src=app.get_asset_url("logo.png"), height="200px"
                                )
                            ),
                            #dbc.Col(
                            #    dbc.NavbarBrand(
                            #        "CSC Analytics", className="ml-2"
                            #    )
                            #),
                        ],
                        #no_gutters=True,
                        className="ml-auto flex-nowrap mt-3 mt-md-0",
                        align="center",
                    ),
                    href=app.get_relative_path("/"),
                ),
                dbc.Nav(
                    children=[
                        dbc.NavLink("Home", href=app.get_relative_path("/"), active="exact", className='active-link'),
                        dbc.NavLink("Seasons", href=app.get_relative_path("/seasons"), active="exact", className='active-link'),
                        dbc.NavLink("Drivers", href=app.get_relative_path("/drivers"), active="exact", className='active-link'),
                        dbc.NavLink(
                            "Constructors", href=app.get_relative_path("/constructors"), active="exact", className='active-link'
                        ),
                        dbc.NavLink(
                            "Circuits", href=app.get_relative_path("/circuits"), active="exact", className='active-link'
                        ),
                    ],
                    style=SIDEBAR_STYLE,
                ),
            ],
           style=CONTENT_STYLE
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
