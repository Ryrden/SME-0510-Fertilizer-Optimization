import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

url = 'https://www.areaseg.com/distancias.html'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# pega cabeçalho
thead = soup.find('thead').find('tr')

# colunas
cidades_coluna = []
for city in thead.find_all('td'):
    cidades_coluna.append(city.text.replace('\n', ''))

# Pega a tabela
tbody = soup.find('tbody')


# Cidades      | Aracaju | Belem | Belo Horizonte
# Ponta grossa |  1000   |  2000 |  3000
# Paulínia     | 1000   |  2000 |  3000
matriz_distancia = []

polos = ['ponta grossa', 'paulínia', 'cubatão', 'rio grande']
for tr in tbody.find_all('tr'):
    linha_cidade = tr.find_all('td')

    if (linha_cidade[0].text.lower() in polos):
        distancias = []

        for dist in linha_cidade:
            distancias.append(dist.text)

        matriz_distancia.append(distancias)

# Deletando a ultima coluna, a qual repete dados
matriz_distancia.pop(-1)
cidades_coluna.pop(-1)

# coloca em arquivo (tabulate)
with open('distancias.md', 'w', -1, "utf-8") as f:
    f.write(tabulate(matriz_distancia, headers=cidades_coluna, tablefmt='github'))
