from dash import Input, Output, callback
import plotly.express as px
import dash
import sys

sys.path.insert(0, '/dados.py')

from dados import Dados

dados = Dados()

@callback(
    Output('Queimadas_Estados', 'figure'),
    Output('Queimadas_Municipios', 'figure'),
    Output('Div_Queimadas_Biomas', 'style'),
    Input('estados', 'value'),
    Input('paises', 'value')
)   
def changeGraph(estados, paises):

    ctx = dash.callback_context

    if not ctx.triggered:
        return defaultGraph()
    
    else:
        action = ctx.triggered[0]['prop_id'].split('.')[0]

        if action == 'estados':
             if estados is not None:
                if len(estados) != 0:
                    return handlerEstadoGraph(estados), defaultGraph('municipio')

        elif action == 'paises':
            if paises is not None:
                if len(paises) != 0:
                    return handlerPaisGraph(paises)
                
        return defaultGraph()


def defaultGraph(type = ''):

    Queimadas_Estados = px.bar(
        dados.getDadosEstados(), 
        title="Queimadas por Estados",
        text_auto=True,
        labels={
            "value": "Ocorrências",
            "estado": "Estados",
        },   
    )

    Queimadas_Municipio = px.bar(
        dados.getDadosMunicipio(), 
        title="Queimadas por Municipio",
        text_auto=True,
        labels={
            "value": "Ocorrências",
            "estado": "Municipio",
        },   
        orientation='h',
    )
    
    Queimadas_Estados.update_layout(showlegend=False)
    Queimadas_Municipio.update_layout(showlegend=False)
    Div_Queimadas_Biomas = { 'display': 'block' }

    if type == 'estados':
        return Queimadas_Estados

    elif type == 'municipio':
        return Queimadas_Municipio
    
    else:
        return Queimadas_Estados, Queimadas_Municipio, Div_Queimadas_Biomas

def handlerEstadoGraph(estados):
    temp = dados.getDados()
    temp.rename(columns = {"satelite": "ocorrencias"}, inplace = True)
    temp = temp.query('estado == '+str(estados))
    temp = temp.groupby(by=["municipio"]).count().filter(["ocorrencias"]).sort_values(by=['ocorrencias'], ascending=False).head(30)

    Queimadas_Estados = px.bar(
                temp, 
                title="Queimadas dos municípios: "+ str(estados),
                text_auto=True,
                labels={
                    "value": "Ocorrências",
                    "estado": "Municípios",
                },   
            )
    
    Queimadas_Estados.update_layout(showlegend=False)

    return Queimadas_Estados

def handlerPaisGraph(paises):
    temp = dados.getDados()
    temp.rename(columns = {"satelite": "ocorrencias"}, inplace = True)
    temp = temp.query('pais == '+str(paises))

    estado = temp.groupby(by=["estado"]).count().filter(["ocorrencias"]).sort_values(by=['ocorrencias'], ascending=False).head(30)
    municipio = temp.groupby(by=["municipio"]).count().filter(["ocorrencias"]).sort_values(by=['ocorrencias'], ascending=False).head(30)
    
    Queimadas_Estados = px.bar(
        estado, 
        title="Queimadas por Estados",
        text_auto=True,
        labels={
            "value": "Ocorrências",
            "estado": "Estados",
        },   
    )

    Queimadas_Municipio = px.bar(
        municipio, 
        title="Queimadas por Municipio",
        text_auto=True,
        labels={
            "value": "Ocorrências",
            "estado": "Municipio",
        },   
        orientation='h',
    )

    Queimadas_Estados.update_layout(showlegend=False)
    Queimadas_Municipio.update_layout(showlegend=False)
    Div_Queimadas_Biomas = { 'display': 'block' }

    for pais in paises:
        if pais != 'Brasil':
            Div_Queimadas_Biomas = { 'display': 'none' }

    return Queimadas_Estados, Queimadas_Municipio, Div_Queimadas_Biomas