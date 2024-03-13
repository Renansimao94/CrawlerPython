import requests
from bs4 import BeautifulSoup

# Define a URL da página que queremos rastrear
url = "https://www.fordzona.sk"  # Substitua pela URL desejada

# Realiza uma requisição GET para a URL
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Cria um objeto BeautifulSoup para analisar o HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Encontra todos os links na página
    links = soup.find_all("a")

    # Imprime os URLs de todos os links encontrados
    for link in links:
        print(link.get("href"))
else:
    print(f"Erro ao acessar a página: {response.status_code}")
