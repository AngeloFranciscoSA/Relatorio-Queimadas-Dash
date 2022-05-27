from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import callbacks.callback
from pages import relatorio_estados, relatorio_municipios, home_page, relatorio_biomas, mapa_mundi, sideBar


external_stylesheets = [
    'https://fonts.googleapis.com/css?family=Source+Sans+Pro',
    'assets/custom.css',
    dbc.themes.COSMO,
    dbc.icons.FONT_AWESOME
]

app = Dash(
        __name__,
        external_stylesheets=external_stylesheets,
        suppress_callback_exceptions=True,
        meta_tags=[
            {"name": "viewport", "content": "width=device-width, initial-scale=1"},
        ],
    )
server = app.server
app.css.config.serve_locally = True

app.layout = dbc.Container([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),

    home_page.layout,
    mapa_mundi.layout,
    dbc.Row(
        [
            dbc.Col(relatorio_estados.layout),
            dbc.Col(relatorio_municipios.layout),
        ]
    ),
    relatorio_biomas.layout,
], fluid=True) 

if __name__ == '__main__':
    app.run_server()