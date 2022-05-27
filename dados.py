import pandas as pd

class Dados:

    def __init__(self) -> None:
        self.df = pd.read_csv(filepath_or_buffer='queimadas.csv', delimiter=',')

    def get_dados(self):
        return self.df

    def get_estados(self):
        list_estados = []

        df = self.df
        df = df.groupby(by=['estado']).count().reset_index(['estado']).filter(['estado']).to_numpy()

        for estado in df:
            list_estados.append(estado[0])
        
        return list_estados

    def get_paises(self):
        list_pais = []

        df = self.df
        df = df.groupby(by=['pais']).count().reset_index(['pais']).filter(['pais']).to_numpy()

        for pais in df:
            list_pais.append(pais[0])

        return list_pais

    def get_dados_estados(self):
        df = self.df
        df.rename(columns = {"satelite": "ocorrencias"}, inplace = True)
        return df.groupby(by=["estado"]).count().filter(["ocorrencias"]).sort_values(by=['ocorrencias'], ascending=False).head(30)

    def get_dados_municipio(self):
        df = self.df
        df.rename(columns = {"satelite": "ocorrencias"}, inplace = True)
        return df.groupby(by=["municipio"]).count().filter(["ocorrencias"]).sort_values(by=['ocorrencias'], ascending=False).head(30)

    def get_dados_biomas(self):
        df = self.df
        df.rename(columns = {"satelite": "ocorrencias"}, inplace = True)
        return df.groupby(by=["bioma"]).count().filter(["ocorrencias"]).reset_index('bioma')    