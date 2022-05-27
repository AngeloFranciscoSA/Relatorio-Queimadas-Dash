import dash_leaflet as dl
import dash_leaflet.express as dlx
import plotly.express as px
from dados import Dados


class Graficos:

    def __init__(self) -> None:
        self.dados = Dados()


    def get_grafico_estados(self):
        fig = px.bar(
            self.dados.get_dados_estados(), 
            title="Queimadas por Estados",
            text_auto=True,
            labels={
                "value": "Ocorrências",
                "estado": "Estados",
            },
            width=500  
        )

        fig.update_layout(showlegend=False)

        return fig

    def get_grafico_municipio(self):
        fig = px.bar(
            self.dados.get_dados_municipio(), 
            title="Queimadas por Municipio",
            text_auto=True,
            labels={
                "value": "Ocorrências",
                "estado": "Municipio",
            },   
            orientation='h',
        )

        fig.update_layout(showlegend=False)

        return fig

    def get_grafico_biomas(self):
        
        fig = px.pie(
            self.dados.get_dados_biomas(), 
            title="Queimadas por Biomas",
            values="ocorrencias",
            names="bioma",
            color_discrete_sequence=px.colors.sequential.RdBu,
        )

        return fig

    def get_grafico_mapa_mundi(self):

        df = self.dados.get_dados()
        df = df.drop(['diasemchuva', 'precipitacao', 'frp'] , axis=1)
        cords = []

        for hora, satelite, pais, estado, municipio, bioma, riscofogo, lat, long in df.to_numpy():
            descricao = 'Estado: '+ str(estado) + \
                    ' - Município: ' + str(municipio) + \
                    ' - Bioma: '+ str(bioma) + \
                    ' - Risco de Fogo: '+ str(riscofogo)
            cords.append(dict(name=descricao, lat=lat, lon=long))

        return dl.Map([
                dl.TileLayer(),
                dl.GeoJSON(data=dlx.dicts_to_geojson(cords), cluster=True, zoomToBoundsOnClick=True),
                dl.FeatureGroup([
                    dl.EditControl(id="edit_control"),
                    dl.Marker(position=[56, 10])
                ]),
            ],
            center=(-19.642588, -58.139112),
            zoom=4,
            style={
                'width': '98%',
                'height': '92%',
                'margin': "auto",
                "display": "block",
                "borderRadius": "30px"
            }
        )   