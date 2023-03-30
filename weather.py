import requests
import json

# insira sua chave de API aqui
API_KEY = "74ae0b982f87c5c54b44cb537da82ca8"
cidade = input("Digite o nome da Cidade: ")

def mostrar_clima(cidade):
    # fazer uma requisição para a API de previsão do tempo
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}"
    resposta = requests.get(url)

    # processar a resposta da API
    dados_clima = json.loads(resposta.content)

    # exibir o clima atual
    temperatura = round(dados_clima["main"]["temp"] - 273.15, 2)
    descricao_clima = dados_clima["weather"][0]["description"]
    print(f"Em {cidade}, a temperatura atual é de {temperatura}°C e o clima está {descricao_clima}.")

# teste do script
mostrar_clima(cidade)


    
