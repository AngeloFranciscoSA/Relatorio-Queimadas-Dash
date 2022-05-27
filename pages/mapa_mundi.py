from dash import html
from graficos import Graficos

layout = html.Div([
        html.H1(
            'Mapa Mundi',
            style={
                'textAlign': 'center'
            }
        ),
        Graficos().getGraficoMapaMundi()
    ], className="mapa-mundi")