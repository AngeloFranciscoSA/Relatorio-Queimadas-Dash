from dash import dcc, html, Input, Output, callback
from graficos import Graficos

layout = html.Div([
    html.H1(
        'Relatorio dos 30 Municípios',
        style={
            'textAlign': 'center'
        }
    ),

    html.P(
        'São os 30 municípios com mais foco de queimada.',
        style={
            'textAlign': 'center'
        }
    ),

    dcc.Graph(
        id='Queimadas_Municipios',
        figure=Graficos().getGraficoMunicipio(),
    )
], className="queimadas")
