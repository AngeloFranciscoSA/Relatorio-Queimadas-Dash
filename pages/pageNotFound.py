from dash import html
import dash_bootstrap_components as dbc

layout = html.Div([
    html.I(className="fa-regular fa-face-frown fa-10x"),
    html.H1('404'),
    html.P('Pagina não encontrada!'),
    dbc.Button("Home Page", size="lg", color="dark", href="/"),
], style={
    'textAlign': 'center',
    'margin-top': '25%',
})