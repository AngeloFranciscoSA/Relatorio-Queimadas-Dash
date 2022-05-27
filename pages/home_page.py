from dash import Input, Output, State, html, dcc, callback
from dados import Dados
import dash_bootstrap_components as dbc

layout = html.Div([
        html.H1(
            'Relatorio de Queimadas'
        ),
        html.P(
            '''
                Um relatorio sobre as queimadas do periodo de 2022-05-02 até 2022-05-06
            '''
        ),

        dbc.Button("Filtros", id="open-offcanvas", n_clicks=0, size="lg"),
        dbc.Offcanvas(
            [
                html.Div(
                    [
                        dbc.Label("Paises:", html_for="paises"),
                        dcc.Dropdown(
                            id='paises',
                            options = Dados().get_paises(),
                            multi=True,
                            placeholder="Selecione um País",
                            className="drop_pais"
                        ),
                    ], className="labels-filtros"
                ),

                html.Div(
                    [
                        dbc.Label("Estados:", html_for="estados"),
                        dcc.Dropdown(
                            id='estados',
                            options = Dados().get_estados(),
                            multi=True,
                            placeholder="Selecione um Estado",
                            className="drop_estados"
                        ),
                    ], className="labels-filtros"
                ),
            ],
            id="offcanvas",
            title="Filtros",
            is_open=False,
            placement="end",
            scrollable=True,
            style={
            'background': "#E5E5E5"
            }
        ),
    ],
    style={
        'textAlign': 'center'
    }
)

@callback(
    Output("offcanvas", "is_open"),
    Input("open-offcanvas", "n_clicks"),
    [State("offcanvas", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open