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

CONTENT_STYLE = {
    "margin-left": "5rem",
    "margin-right": "3rem",
    "padding": "2rem 1rem",
}

LOGO = app.get_asset_url("logo2.png")

server = app.server

# cambiar raiz

nav_item = dbc.NavItem(
    children=[
        dbc.NavItem(dbc.NavLink("Inicio", href=app.get_relative_path("/"))),
        dbc.NavItem(dbc.NavLink("Seasons", href=app.get_relative_path("/seasons"))),
        dbc.NavItem(dbc.NavLink("Constructors", href=app.get_relative_path("/constructors"))),
        dbc.NavItem(dbc.NavLink("Circuits", href=app.get_relative_path("/circuits"))),
    ]
)

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

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=LOGO, height="130px")),
                        dbc.Col(dbc.NavbarBrand("Multiplo", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href=app.get_relative_path("/multiplo"),
                style={"textDecoration": "none"},
            ),
            dbc.Row(
                [
                    dbc.NavbarToggler(id="navbar-toggler"),
                    dbc.Collapse(
                        dbc.Nav(
                            [
                                dbc.NavItem(dbc.NavLink("Inicio", href=app.get_relative_path("/"))),
                                dbc.NavItem(dbc.NavLink("Seasons", href=app.get_relative_path("/seasons"))),
                                dbc.NavItem(dbc.NavLink("Constructors", href=app.get_relative_path("/constructors"))),
                                dbc.NavItem(dbc.NavLink("Circuits", href=app.get_relative_path("/circuits"))),
                                dbc.NavItem(
                                    dbc.NavLink("Circuits", href=app.get_relative_path("/circuits")),
                                    # add an auto margin after page 2 to
                                    # push later links to end of nav
                                    className="me-auto",
                                ),
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
