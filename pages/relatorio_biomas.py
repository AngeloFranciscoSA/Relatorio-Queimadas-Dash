from dash import dcc, html
from graficos import Graficos

layout = html.Div([
        html.H1(
            'Relatorio dos Biomas',
            style={
                'textAlign': 'center'
            }
        ),
        dcc.Graph(
            id='Queimadas_Biomas',
            figure=Graficos().get_grafico_biomas(),
        )
    ], className="queimadas", id='Div_Queimadas_Biomas')