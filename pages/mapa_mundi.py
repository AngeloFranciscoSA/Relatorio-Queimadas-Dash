from dash import html
from graficos import Graficos

layout = html.Div([
        html.H1(
            'Mapa Mundi',
            style={
                'textAlign': 'center'
            }
        ),
        Graficos().get_grafico_mapa_mundi()
    ], className="mapa-mundi")