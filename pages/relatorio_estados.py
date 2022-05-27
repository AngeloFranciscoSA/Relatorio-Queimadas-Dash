from dash import dcc, html
from graficos import Graficos
from dados import Dados

layout = html.Div([
        html.H1(
            'Relatorio dos Estados',
            style={
                'textAlign': 'center'
            }
        ),

        html.P(
            'São os 30 estados com mais foco de queimada.',
            style={
                'textAlign': 'center'
            }
        ),
    
        dcc.Graph(
            id='Queimadas_Estados',
            figure=Graficos().getGraficoEstados(),
        )
    ], className="queimadas")