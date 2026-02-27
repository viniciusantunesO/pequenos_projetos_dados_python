import requests #É uma biblioteca q faz requisicoes HTTP ("conversa" com a API) 


def buscar_cotacao(moeda):
    url=f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL" 
    resposta=requests.get(url) #Envia um requisiçao HTTP GET para a API
    dados=resposta.json() #Trasnforma a rewquisiçao em um dicionario

    chave=f"{moeda}BRL"
    return dados[chave]

def converter(valor_em_reais, cotacao):
    return valor_em_reais/ float(cotacao)

moeda=input("Digite a moeda (USD, EUR, BTC): ").upper()
dados=buscar_cotacao(moeda)

print("Valor atual: ", dados["bid"])
print("Valor maximo: ", dados["high"])
print("Valor minimo: ", dados["low"])

valor_em_reais=float(input("Digite quanto vc quer converter para real: "))
convertido=converter(valor_em_reais, dados["bid"])

print("Convertido:", convertido, moeda)