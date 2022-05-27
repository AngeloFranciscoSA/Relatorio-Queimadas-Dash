import pandas as pd

class Dados:

    def __init__(self) -> None:
        self.df = pd.read_csv(filepath_or_buffer='queimadas.csv', delimiter=',')

    def getDados(self):
        return self.df

    def getEstados(self):

        arrayEstados = []

        temp = self.df
        temp = temp.groupby(by=['estado']).count().reset_index(['estado']).filter(['estado']).to_numpy()

        for estado in temp:
            arrayEstados.append(estado[0])
        
        return arrayEstados

    def getPaises(self):
        arrayPais = []

        temp = self.df
        temp = temp.groupby(by=['pais']).count().reset_index(['pais']).filter(['pais']).to_numpy()

        for pais in temp:
            arrayPais.append(pais[0])

        return arrayPais


    def getDadosEstados(self):
        temp = self.df
        temp.rename(columns = {"satelite": "ocorrencias"}, inplace = True)
        return temp.groupby(by=["estado"]).count().filter(["ocorrencias"]).sort_values(by=['ocorrencias'], ascending=False).head(30)

    def getDadosMunicipio(self):
        temp = self.df
        temp.rename(columns = {"satelite": "ocorrencias"}, inplace = True)
        return temp.groupby(by=["municipio"]).count().filter(["ocorrencias"]).sort_values(by=['ocorrencias'], ascending=False).head(30)

    def getDadosBiomas(self):
        temp = self.df
        temp.rename(columns = {"satelite": "ocorrencias"}, inplace = True)
        return temp.groupby(by=["bioma"]).count().filter(["ocorrencias"]).reset_index('bioma')    