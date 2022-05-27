# Informações do Projeto

Este projeto é um relatório sobre as queimadas disponibilizada no portal do INPE de Queimadas.

Pode ser acessado por este [link](https://queimadas.dgi.inpe.br/queimadas/bdqueimadas) ou por aqui https://queimadas.dgi.inpe.br/queimadas/bdqueimadas

O objetivo deste projeto é criar um dashboard para exibir informações das queimadas dentro do período de 02/05/2022 até 06/05/2022.

Todas essas informações podem ser obtidas de maneira gratuita atras do portal Queimadas.

# Informações Técnica

O projeto foi realizado em Python 3.6+ e utiliza estas bibliotecas externas:
  * dash = 2.3.1
  * dash-bootstrap-components = 1.1.0
  * dash-leaflet = 0.1.23
  * pandas = 1.4.1  

Para iniciar o projeto basta instalar as bibliotecas e executar o seguinte comando o seu terminal:
```
 python app.py
```

# Procedencia dos dados

Os dados mostradas neste dashbord vem de um arquivo csv que foi retirado do portal DBQueimadas do INPE dentro do período de 02/05/2022 até 06/05/2022.
