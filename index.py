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
import dash_mantine_components as dmc
from dash_iconify import DashIconify

CONTENT_STYLE = {
    "margin-left": "5rem",
    "margin-right": "3rem",
    "padding": "2rem 1rem",
}

LOGO = app.get_asset_url("logo0.png")

server = app.server

# make a reuseable dropdown for the different examples
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Entry 1"),
        dbc.DropdownMenuItem("Entry 2"),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Entry 3"),
    ],
    nav=True,
    in_navbar=True,
    label="Menu",
)

productos = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem(
            dbc.NavItem(dbc.NavLink("Tableros Analíticos", href=app.get_relative_path("/tableros_analiticos"))),
        ),
        dbc.DropdownMenuItem(
            dbc.NavItem(dbc.NavLink("Tableros Inteligentes", href=app.get_relative_path("/tableros_inteligentes"))),
        ),        
    ],
    nav=True,
    in_navbar=True,
    label="Productos",
)

soluciones = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem(
            dbc.NavItem(dbc.NavLink("Genéricas", href=app.get_relative_path("/soluciones"))),
        ),       
        dbc.DropdownMenuItem(divider=True),        
    ],
    nav=True,
    in_navbar=True,
    label="Soluciones",
)

#className="fa fa-fw fa-home"

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        #dbc.Col(html.Img(src=LOGO, height="80px")),
                        dbc.Col(dbc.NavbarBrand(
                            "yflow", 
                            className="ms-2",
                            style={"font-size": "50px"},
                        )),
                    ],
                    align="center",
                    className="g-0",
                ),
                #href=app.get_relative_path("/multiplo"),
                style={"textDecoration": "none"},
            ), 
            dbc.Button(DashIconify(icon="material-symbols:home"), 
                outline=True,                
                color= "info",
                size= "lg", 
                href= app.get_relative_path("/"), 
                external_link=True,  
                style={"border": "none"},                                                         
                #disabled=True,
            ),
            dbc.NavItem(
                dbc.Nav(
                    [
                        productos
                    ], 
                    className="ms-auto", 
                    navbar=True),  
            ),  
            dbc.NavItem(
                dbc.Nav(
                    [
                        soluciones
                    ], 
                    className="ms-auto", 
                    navbar=True),  
            ),                
            dbc.NavItem(
                dbc.NavLink(
                    "Quienes somos", 
                    href=app.get_relative_path("/multiplo" )
                ),
                className="me-auto",
            ),
            dbc.Row(                
                [
                    dbc.Collapse(
                        dbc.Nav(
                            [  
                                dbc.Collapse(
                                    dbc.Nav(
                                        [
                                            dropdown
                                        ], 
                                        className="ms-auto", 
                                        navbar=True),
                                    id="navbar-collapse1",
                                    navbar=True,
                                ),
                                # Cambiar estos elementos
                                dbc.NavItem(dbc.NavLink("Help")),
                                dbc.NavItem(dbc.NavLink("About")),
                            ],
                            # make sure nav takes up the full width for auto
                            # margin to get applied
                            className="w-100",
                        ),
                        id="navbar-collapse",
                        is_open=False,
                        navbar=True,
                    ),
                ],
                # the row should expand to fill the available horizontal space
                className="flex-grow-1",
            ),
        ],
        fluid=True,
    ),
    dark=True,
    color="dark",
     style={"border": "none"},
    #style=CONTENT_STYLE,
)

app.layout = html.Div(
    [
        dcc.Location(
           id="url", 
           refresh=False
        ), 
        navbar,             
        html.Div(
           id="page-content", 
           style=CONTENT_STYLE
        ),
    ]
)

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])

def display_page_content(pathname):
    path = app.strip_relative_path(pathname)
    if not path:
        return pages.home.layout()
    elif path == "multiplo":
        return pages.multiplo.layout()
    elif path == "soluciones":
        return pages.soluciones.layout()    
    elif path == "tableros_analiticos":
        return pages.tableros_analiticos.layout()
    elif path == "tableros_inteligentes":
        return pages.tableros_inteligentes.layout()
    else:
        return "404"


if __name__ == "__main__":
    app.run_server(debug=True)
